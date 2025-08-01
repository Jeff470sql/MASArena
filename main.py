#!/usr/bin/env python3
import argparse
import datetime
import sys
from pathlib import Path
import asyncio

from mas_arena.benchmark_runner import BenchmarkRunner
import logging

logger = logging.getLogger(__name__)


def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Run benchmarks for multi-agent systems")

    # Import available agent systems and benchmarks
    from mas_arena.agents import AVAILABLE_AGENT_SYSTEMS
    from mas_arena.evaluators import BENCHMARKS
    parser.add_argument(
        "--benchmark",
        type=str,
        default="math",
        choices=list(BENCHMARKS.keys()),
        help="Benchmark to run (default: math)",
    )

    parser.add_argument(
        "--data", type=str, default=None, help="Path to benchmark data (default: data/{benchmark}_test.jsonl)"
    )

    parser.add_argument("--limit", type=int, default=None, help="Maximum number of problems to process (default: None)")

    parser.add_argument(
        "--agent-system",
        type=str,
        default="single_agent",
        choices=list(AVAILABLE_AGENT_SYSTEMS.keys()),
        help="Agent system to use (default: single_agent)",
    )

    parser.add_argument(
        "--verbose", action="store_true", default=True, help="Print progress information (default: True)"
    )

    parser.add_argument(
        "--results-dir", type=str, default="results", help="Directory to store results (default: results)"
    )

    parser.add_argument(
        "--use-mcp-tools", action="store_true", default=False,
        help="Enable integration of MCP tools (default: False)"
    )

    parser.add_argument(
        "--mcp-config-file", type=str, default=None,
        help="Path to MCP servers configuration JSON file"
    )

    parser.add_argument(
        "--use-tools", action="store_true", default=None,
        help="Enable integration of tools (default: False)"
    )

    parser.add_argument(
        "--async-run", action="store_true", help="Run the benchmark asynchronously."
    )
    parser.add_argument(
        "--concurrency", type=int, default=10, help="Concurrency level for async run."
    )

    parser.add_argument(
        "--data-id", type=str, default=None,
        help="Data ID to use (default: None)"
    )

    # Parse arguments
    args = parser.parse_args()

    # Build agent configuration for MCP tool integration
    agent_config = {}
    if args.use_mcp_tools:
        agent_config["use_mcp_tools"] = True
        import json
        if not args.mcp_config_file:
            parser.error("--use-mcp-tools requires --mcp-config-file")
        try:
            with open(args.mcp_config_file, "r") as f:
                agent_config["mcp_servers"] = json.load(f)
                
            # Store the config file path for reference
            agent_config["mcp_config_file"] = args.mcp_config_file
            
            # Enable mock mode if "mock" appears in the config file name
            if "mock" in args.mcp_config_file.lower():
                agent_config["mock_mcp"] = True
                print(f"Using mock MCP tools (config: {args.mcp_config_file})")
                
        except Exception as e:
            print(f"Failed to load MCP config file: {e}", file=sys.stderr)
            return 1

    if args.use_tools:
        agent_config["use_tools"] = True

    # Create directories if needed
    Path(args.results_dir).mkdir(exist_ok=True)

    # Print header
    
    print("\n" + "=" * 80)
    print(f"Multi-Agent Benchmark Runner ({datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})")
    print("=" * 80)
    print(f"Benchmark: {args.benchmark}")
    print(f"Agent System: {args.agent_system}")
    print(f"Data: {args.data or 'default'}")
    print(f"Limit: {args.limit or 'all'}")
    print("=" * 80 + "\n")

    # Create benchmark runner
    runner = BenchmarkRunner(results_dir=args.results_dir)

    # Check for concurrency support
    benchmark_config = BENCHMARKS.get(args.benchmark, {})
    evaluator_class = benchmark_config.get("evaluator")
    supports_concurrency = evaluator_class and getattr(evaluator_class, 'SUPPORTS_CONCURRENCY', True)

    run_async = args.async_run and supports_concurrency
    if args.async_run and not supports_concurrency:
        if args.verbose:
            print(f"Warning: {args.benchmark} benchmark does not support concurrency. Running synchronously.\n")

    # Run benchmark
    try:
        if run_async:
            summary = asyncio.run(runner.arun(
                benchmark_name=args.benchmark,
                data_path=args.data,
                limit=args.limit,
                agent_system=args.agent_system,
                agent_config=agent_config if agent_config else None,
                verbose=args.verbose,
                concurrency=args.concurrency,
            ))
        else:
            summary = runner.run(
                benchmark_name=args.benchmark,
                data_path=args.data,
                limit=args.limit,
                agent_system=args.agent_system,
                agent_config=agent_config if agent_config else None,
                verbose=args.verbose
            )
        logger.info(f"Benchmark summary: {summary}")
        return 0

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())

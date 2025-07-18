#!/bin/bash
# Benchmark Runner Script
# Usage: ./run_benchmark.sh [benchmark_name] [agent_system] [limit] [mcp_config_file] [concurrency]

# Default values
BENCHMARK=${1:-math}
AGENT_SYSTEM=${2:-agentverse} # single_agent, supervisor_mas, swarm, agentverse
LIMIT=${3:-2}
MCP_CONFIG=${4:-}
CONCURRENCY=${5:-6}

# Create necessary directories
mkdir -p results metrics

# Print header
echo "====================================================="
echo "Running Multi-Agent Benchmark"
echo "====================================================="
echo "Benchmark: $BENCHMARK"
echo "Agent System: $AGENT_SYSTEM"
echo "Limit: $LIMIT"
if [ -n "$MCP_CONFIG" ]; then
  echo "MCP Config File: $MCP_CONFIG"
  echo "Using MCP tools: yes"
else
  echo "Using MCP tools: no"
fi
if [ -n "$CONCURRENCY" ]; then
  echo "Concurrency: $CONCURRENCY"
  echo "Running asynchronously: yes"
else
  echo "Running asynchronously: no"
fi
echo "====================================================="

# Activate virtual environment if exists
if [ -d ".venv" ]; then
  source .venv/bin/activate
fi

# Build MCP flags if config provided
if [ -n "$MCP_CONFIG" ]; then
  MCP_FLAGS="--use-mcp-tools --mcp-config-file $MCP_CONFIG"
else
  MCP_FLAGS=""
fi

# Build concurrency flags if provided
if [ -n "$CONCURRENCY" ]; then
  ASYNC_FLAGS="--async-run --concurrency $CONCURRENCY"
else
  ASYNC_FLAGS=""
fi

# Run the benchmark
python main.py \
  --benchmark "$BENCHMARK" \
  --agent-system "$AGENT_SYSTEM" \
  --limit "$LIMIT" \
  $MCP_FLAGS \
  $ASYNC_FLAGS

# Exit with the same status as the Python script
exit $? 
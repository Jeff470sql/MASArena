# Multi-Agent Benchmark

A comprehensive framework for benchmarking single and multi-agent systems across various tasks, evaluating their performance, accuracy, and efficiency.

## 🚀Quick Start

### Setup

We highly recommend using [uv](https://docs.astral.sh/uv/) to manage project dependencies:

```bash
# Install dependencies
uv sync

# Setup pre-commit hooks
pre-commit install
```

When you want to add a dependency to the project:

```bash
uv add [package]
```

The packages installed by `pip` would NOT be added into project dependencies.

Set your environmental variable at .env
```bash
OPENAI_API_KEY=YOUR_OPENAI_API_KEY
MODEL_NAME=gpt-4o-mini
OPENAI_API_BASE=https://api.openai.com/v1
```

### Running Benchmarks

The main way to run benchmarks is through the `main.py` script:

```bash
# Run a math benchmark with the single agent system
python main.py --benchmark math --agent-system single_agent --limit 5

# Run a benchmark with the supervisor-based multi-agent system
python main.py --benchmark math --agent-system supervisor_mas --limit 10

# Run with swarm-based agent system
python main.py --benchmark math --agent-system swarm --limit 5

```

You can also use the runner scripts for more options:

```bash
# Using the bash runner
./run_benchmark.sh math swarm 5
```



### Visualizing Agent Interactions

The framework provides interactive visualizations for agent interactions and benchmark results:

```bash
python benchmark/src/visualization/visualize_benchmark.py visualize --summary results/math_swarm_20250423_170316_summary.json
```



## 📊 Supported Benchmarks

| Benchmark | Description | Data File |
|-----------|-------------|-----------|
| `math` | Mathematical problem solving | `math_test.jsonl` |
| `humaneval` | Python code generation | `humaneval_test.jsonl` |
| `mbpp` | Python programming problems | `mbpp_test.jsonl` |
| `gsm8k` | Elementary math problems | `gsm8k_test.jsonl` |
| `drop` | Reading comprehension | `drop_test.jsonl` |
| `bbh` | Complex reasoning tasks | `bbh_test.jsonl` |
| `hotpotqa` | Multi-hop question answering | `hotpotqa_test.jsonl` |
| `ifeval` | Instruction following | `ifeval_test.jsonl` |
| `aime` | Math competition problems | `aime_*_test.jsonl` |
| `mmlu_pro` | Multi-domain knowledge | `mmlu_pro_test.jsonl` |
| `swebench` | Software engineering | `swebench_lite_test.jsonl` |

## 🤖 Supported Agent Systems

| Agent System | File Location | Description |
|--------------|---------------|-------------|
| `single_agent` | `single_agent.py` | Single LLM agent |
| `supervisor_mas` | `supervisor_mas.py` | Supervisor-based multi-agent system |
| `swarm` | `swarm.py` | Swarm-based multi-agent system |
| `agentverse` | `AgentVerse.py` | Dynamic recruitment agent system |
| `chateval` | `ChatEval.py` | Debate-based multi-agent system |
| `evoagent` | `EvoAgent.py` | Evolutionary agent system |
| `jarvis` | `JARVIS.py` | Task planning agent system |
| `metagpt` | `MetaGPT.py` | Code generation agent system |


## System Overview

Check out the [System Overview](docs/architecture/system_overview.md) for a detailed overview of the project.




## Extending the Framework

### Adding a New Agent System

1. Create a new file in `benchmark/src/agents/` (e.g., `my_agent.py`)
2. Implement your agent system by subclassing `AgentSystem` from `base.py`
3. Register your system with the `AgentSystemRegistry`
4. Import your agent system in `__init__.py` to make it available

### Adding a New Benchmark Dataset

1. Add your dataset to `results/`
2. Create a corresponding evaluator in `benchmark/src/evaluators/`
3. Update the available choices in `main.py`

## Tool Integration

Use the `--use-mcp-tools` and `--mcp-config-file` flags when running benchmarks:
```bash
./run_benchmark.sh math mock_triple_agent 1 mock_mcp_config.json

>>> Output:
[ToolIntegration] Worker 'MathAgent' received 3 tools: mock_add, mock_subtract, mock_math_solve
[ToolIntegration] Worker 'SearchAgent' received 1 tools: mock_search
[ToolIntegration] Worker 'ReasoningAgent' received 1 tools: mock_reason
```

## Tool Selection and Distribution
- You can override the default tool selection and distribution by implementing your own `ToolSelector` and `ToolIntegrationWrapper`.
- Check out the [Tool Integration](docs/tools/tool_integration.md) for a detailed overview of the tool integration system.

# TODOs

- [ ] Asynchronous mode for model calls. 
- [ ] Failure detection for MAS interactions.
- [ ] Add more benchmarks targeting tools. 
- [ ] Configuration setup for MAS and tool integration. 
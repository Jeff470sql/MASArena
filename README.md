# <div align="center">

  <h1 align="center">MASArena 🏟️</h1>
  <!-- <p align="center"><i>Multi-Agent Systems Arena</i></p> -->
  <p align="center">
    <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/python-3.11+-blue" alt="Python 3.11+" height="20"/></a>
    <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow" alt="License: MIT" height="20"/></a>
    <a href="https://lins-lab.github.io/MASArena"><img src="https://img.shields.io/badge/📖%20Docs-MASArena-blue" alt="Documentation" height="20"/></a>
    <a href="https://deepwiki.com/LINs-lab/MASArena"><img src="https://deepwiki.com/badge.svg" alt="Ask DeepWiki" height="20"></a>
  </p>
  
  
  <p align="center">
    <b>Layered Architecture</b> • <b>Stack</b> • <b>Swap</b> • <b>Built for Scale</b>
  </p>
  <img src="docs/images/intro.svg" style="display: block; margin: 0 auto; max-width: 100%;" alt="MASArena Architecture"/>
</div>

## 🌟 Core Features

* **🧱 Modular Design**: Swap agents, tools, datasets, prompts, and evaluators with ease.
* **📦 Built-in Benchmarks**: Single/multi-agent datasets for direct comparison.
* **📊 Visual Debugging**: Inspect interactions, accuracy, and tool use.
* **🔧 Tool Support**:  Manage tool selection via pluggable wrappers.
* **🧩 Easy Extensions**: Add agents via subclassing—no core changes.
* **📂 Paired Datasets & Evaluators**: Add new benchmarks with minimal effort.
* **🔍 Failure Attribution**: Identify failure causes and responsible agents.

## 🎬 Demo

See MASArena in action! This demo showcases the framework's visualization capabilities:

https://github.com/user-attachments/assets/b6e56eef-e00e-46bb-97e0-02d2aca47403

## 🚀 Quick Start

### 1. Setup

We recommend using [uv](https://docs.astral.sh/uv/) for dependency and virtual environment management.

```bash
# Install dependencies
uv sync

# Activate the virtual environment
source .venv/bin/activate
```

### 2. Configure Environment Variables

Create a `.env` file in the project root and set the following:

```bash
OPENAI_API_KEY=your_openai_api_key
MODEL_NAME=gpt-4o-mini
OPENAI_API_BASE=https://api.openai.com/v1
```

### 3. Running Benchmarks

```bash
./run_benchmark.sh
```
* Supported benchmarks: 
  * Math: `math`, `aime`
  * Code: `humaneval`, `mbpp`
  * Reasoning: `drop`, `bbh`, `mmlu_pro`, `ifeval`
* Supported agent systems: 
  * Single Agent: `single_agent`
  * Multi-Agent: `supervisor_mas`, `swarm`, `agentverse`, `chateval`, `evoagent`, `jarvis`, `metagpt`

## 🧪 Testing

MASArena includes a comprehensive test suite to ensure code reliability and facilitate development.

### Running Tests

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=mas_arena --cov-report=html

# Run only unit tests
pytest -m "unit"

# Run only integration tests
pytest -m "integration"

# Run tests excluding slow tests
pytest -m "not slow"

# Run specific test file
pytest tests/test_agents.py

# Run with verbose output
pytest -v
```

### Test Structure

- `tests/test_agents.py` - Tests for agent systems
- `tests/test_evaluators.py` - Tests for evaluation components
- `tests/test_tools.py` - Tests for tool management
- `tests/test_benchmark_runner.py` - Tests for benchmark execution
- `tests/test_integration.py` - End-to-end integration tests
- `tests/conftest.py` - Shared fixtures and configuration

### Test Categories

- **Unit Tests**: Fast, isolated tests for individual components
- **Integration Tests**: Tests for component interactions
- **Slow Tests**: Long-running tests (marked with `@pytest.mark.slow`)

## 📚 Documentation

For comprehensive guides, tutorials, and API references, visit our complete [documentation](https://lins-lab.github.io/MASArena).

## ✅ TODOs

* [x] Add asynchronous support for model calls
* [x] Implement failure detection in MAS workflows
* [ ] Add more benchmarks emphasizing tool usage
* [ ] Improve configuration for MAS and tool integration
* [ ] Integrate multiple tools(e.g., Browser, Video, Audio, Docker) into the current evaluation framework
* [ ] Optimize the framework's tool management architecture to decouple MCP tool invocation from local tool invocation
* [ ] Implement more benchmark evaluations(e.g., webArena, SweBench) that requires tool usage
* [ ] Reimplementation of the Dynamic Architecture Paper Based on the Benchmark Framework

## 🙌 Contributing

We warmly welcome contributions from the community!

You can contribute in many ways:

* 🧠 **New Agent Systems (MAS):**
  Add novel single- or multi-agent systems to expand the diversity of strategies and coordination models.

* 📊 **New Benchmark Datasets:**
  Bring in domain-specific or task-specific datasets (e.g., reasoning, planning, tool-use, collaboration) to broaden the scope of evaluation.

* 🛠 **New Tools & Toolkits:**
  Extend the framework's tool ecosystem by integrating domain tools (e.g., search, calculators, code editors) and improving tool selection strategies.

* ⚙️ **Improvements & Utilities:**
  Help with performance optimization, failure handling, asynchronous processing, or new visualizations.

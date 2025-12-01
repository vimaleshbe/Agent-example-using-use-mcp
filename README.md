# use-mcp

A Python project demonstrating how to use the [MCP (Model Context Protocol)](https://github.com/modelcontextprotocol) with LangChain and OpenAI-compatible LLMs.

## Overview

This project showcases the integration of MCP servers with language models using the `mcp-use` library. It provides a simple example of how to:

- Configure and connect to MCP servers
- Use LangChain's ChatOpenAI with a local or remote LLM endpoint
- Create an MCPAgent to interact with MCP tools

## Prerequisites

- Python 3.13 or higher
- Node.js (for running MCP servers via npx)
- A running OpenAI-compatible LLM server (e.g., at `http://localhost:4141/v1/`)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/vimaleshbe/use-mcp.git
   cd use-mcp
   ```

2. Install dependencies using [uv](https://github.com/astral-sh/uv) (recommended):
   ```bash
   uv sync
   ```

   Or using pip:
   ```bash
   pip install langchain-openai>=1.1.0 mcp-use>=1.4.1
   ```

## Configuration

The project uses a configuration dictionary to define MCP servers. The example in `main.py` configures the `sequential-thinking` server:

```python
config = {
    "mcpServers": {
        "sequential-thinking": {
            "command": "npx",  # Use full path on Windows, e.g., "C:\\Program Files\\nodejs\\npx.cmd"
            "args": [
                "-y",
                "@modelcontextprotocol/server-sequential-thinking"
            ]
        }
    }
}
```

> **Note:** On Windows, you may need to use the full path to `npx.cmd`, such as `"C:\\Program Files\\nodejs\\npx.cmd"`.

### LLM Configuration

The example uses a local OpenAI-compatible endpoint:

```python
llm = ChatOpenAI(
    model="your-model-name",  # e.g., "gpt-4", "llama-2", or your local model
    base_url="http://localhost:4141/v1/",
    api_key="dummy"  # Use a real API key if required by your endpoint
)
```

Modify these settings to match your LLM setup. The `base_url` should point to your OpenAI-compatible API server.

## Usage

Run the example script:

```bash
python main.py
```

Or using uv:

```bash
uv run main.py
```

This will:
1. Start the configured MCP server
2. Connect the LLM to the MCP client
3. Execute the query "List all my tools"
4. Print the result

## Dependencies

- [langchain-openai](https://pypi.org/project/langchain-openai/) (>=1.1.0) - LangChain integration for OpenAI models
- [mcp-use](https://pypi.org/project/mcp-use/) (>=1.4.1) - MCP client library for Python

## License

This project is provided as-is for demonstration purposes.

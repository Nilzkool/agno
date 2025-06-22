# DeepSeek Cookbook

> Note: Fork and clone this repository if needed

### 1. Create and activate a virtual environment

```shell
python3 -m venv ~/.venvs/aienv
source ~/.venvs/aienv/bin/activate
```

### 2. Export your `DEEPSEEK_API_KEY`

```shell
export DEEPSEEK_API_KEY=***
```

### 3. Install libraries

```shell
pip install -U openai duckduckgo-search duckdb yfinance agno
```

### 4. Run basic Agent

- Streaming on

```shell
python cookbook/models/deepseek/basic_stream.py
```

- Streaming off

```shell
python cookbook/models/deepseek/basic.py
```

### 5. Run Agent with Tools

- DuckDuckGo Search

```shell
python cookbook/models/deepseek/tool_use.py
```

### 6. Structured output support

> Note: DeepSeek's native structured output support is currently broken.
> The structured_output example may not produce structured outputs.

```shell
python cookbook/models/deepseek/structured_output.py
```

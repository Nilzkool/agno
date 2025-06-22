# Fireworks AI Cookbook

> Note: Fork and clone this repository if needed

### 1. Create and activate a virtual environment

```shell
python3 -m venv ~/.venvs/aienv
source ~/.venvs/aienv/bin/activate
```

### 2. Export your `FIREWORKS_API_KEY`

```shell
export FIREWORKS_API_KEY=***
```

### 3. Install libraries

```shell
pip install -U openai duckduckgo-search duckdb yfinance agno
```

### 4. Run basic Agent

- Non-streaming

```shell
python cookbook/models/fireworks/basic.py
```

### 5. Run basic async Agent

- Non-streaming

```shell
python cookbook/models/fireworks/async_basic.py
```

- Streaming

```shell
python cookbook/models/fireworks/async_basic_stream.py
```

# Hackathon Resources

Thank you for using Agno to build your hackathon project! Here you'll find setup guides and workshop examples to bring your multimodal agents to life.

> Read this documentation on [Agno Docs](https://docs.agno.com)

## Environment Setup

Let's get your environment setup for the hackathon. Here are the steps:

1. Create a virtual environment
2. Install libraries
3. Export your API keys

### Create a virtual environment

You can use `python3 -m venv` or `uv` to create a virtual environment.

- Standard python

```shell
python3 -m venv .venv
source .venv/bin/activate
```

- Using uv

```shell
uv venv --python 3.12
source .venv/bin/activate
```

- For Windows

```shell
python -m venv venv
venv\scripts\activate
```

### Install libraries

Install the `agno` python package along with the models and tools you want to use.

- Standard python

```shell
pip install -U agno openai
```

- Using uv

```shell
uv pip install -U agno openai
```

### Export your API keys

Export the API keys for the models and tools you want to use.

```shell
export OPENAI_API_KEY=***
export GOOGLE_API_KEY=***
export ELEVEN_LABS_API_KEY=***
```

For Windows

```shell
$env:OPENAI_API_KEY="your-api-key"
```

## Workshop Examples

Here are the code examples for the hackathon workshop:

- [Agno Assist - Basic](workshop/agno_assist.py)
- [Agno Assist with Voice](workshop/agno_assist_voice.py)
- [Workshop Playground](workshop/playground.py)

## Data Samples

Sample data files are available under `data/`:

- `sample_audio.wav`
- `sample_image.jpg`

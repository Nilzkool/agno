# SQrL: A Text2SQL Reasoning Agent

SQrL is an advanced text-to-SQL system that leverages Reasoning Agents to provide deep insights into any data. We'll use the F1 dataset as an example, but the system is designed to be easily extensible to other datasets.

The agent uses Reasoning Agents to search for table metadata and rules, enabling it to write and run better SQL queries. This process, called `Dynamic Few Shot Prompting`, is a technique that allows the agent to dynamically search for few-shot examples to improve its performance.

SQrL also "thinks" before it acts. It will think about the user's question, and then decide to search its knowledge base before writing and running the SQL query.

SQrL also "analyzes" the result of the SQL query, which yields much better results.

> Note: Fork and clone the repository if needed

### 1. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install libraries

```bash
pip install -r cookbook/examples/apps/sql_agent/requirements.txt
```

### 3. Launch PgVector

> Install [Docker Desktop](https://docs.docker.com/desktop/install/) first.

```bash
# Using Docker
docker run -d \
  -e POSTGRES_DB=ai \
  -e POSTGRES_USER=ai \
  -e POSTGRES_PASSWORD=ai \
  -e PGDATA=/var/lib/postgresql/data/pgdata \
  -v pgvolume:/var/lib/postgresql/data \
  -p 5532:5432 \
  --name pgvector \
  agnohq/pgvector:16
```

### 4. Load F1 data

```bash
python cookbook/examples/apps/sql_agent/load_f1_data.py
```

### 5. Load the knowledge base

```bash
python cookbook/examples/apps/sql_agent/load_knowledge.py
```

### 6. Export API Keys

```bash
export ANTHROPIC_API_KEY=***
```

Other API keys are optional:

```bash
export OPENAI_API_KEY=***
export GOOGLE_API_KEY=***
export GROQ_API_KEY=***
```

### 7. Run SQL Agent

```bash
streamlit run cookbook/examples/apps/sql_agent/app.py
```

Open [localhost:8501](http://localhost:8501) to view the SQL Agent.

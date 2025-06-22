# Agent Knowledge

**Knowledge Base:** is information that the Agent can search to improve its responses. This directory contains a series of cookbooks that demonstrate how to build a knowledge base for the Agent.

> Note: Fork and clone this repository if needed

### 1. Create a virtual environment

```shell
python3 -m venv ~/.venvs/aienv
source ~/.venvs/aienv/bin/activate
```

### 2. Install libraries

```shell
pip install -U pgvector "psycopg[binary]" sqlalchemy openai agno
```

### 3. Run PgVector

> Install [docker desktop](https://docs.docker.com/desktop/install/mac-install/) first.

- Run using a helper script

```shell
./cookbook/run_pgvector.sh
```

- OR run using the docker run command

```shell
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

### 4. Test Knowledge Cookbooks (PDF URL Knowledge Base)

- Install libraries

```shell
pip install -U pypdf bs4
```

- Run the PDF URL script

```shell
python cookbook/agent_concepts/knowledge/pdf_url.py
```

### 5. Test Chunking Strategies

These examples show how to split documents into chunks before indexing:

- Agentic Chunking

```shell
python cookbook/agent_concepts/knowledge/chunking/agentic_chunking.py
```

- Recursive Chunking

```shell
python cookbook/agent_concepts/knowledge/chunking/recursive_chunking.py
```

- Document Chunking

```shell
python cookbook/agent_concepts/knowledge/chunking/document_chunking.py
```

### 6. Test Vector DB Configuration

Demonstrates custom vector database setups:

- PgVector DB (default table)

```shell
python cookbook/agent_concepts/knowledge/vector_dbs/pgvector_db/pg_vector.py
```

# Agentic RAG Agent

**Agentic RAG Agent** is a chat application that combines models with retrieval-augmented generation.
It allows users to ask questions based on custom knowledge bases, documents, and web data, retrieve context-aware answers, and maintain chat history across sessions.

> Note: Fork and clone this repository if needed

### 1. Change directory

```shell
cd cookbook/examples/apps/agentic_rag
```

### 2. Create a virtual environment

```shell
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```shell
pip install -r requirements.txt
```

### 4. Run PgVector

> Install [Docker Desktop](https://docs.docker.com/desktop/install/) first.

Start a PostgreSQL container with the pgvector extension:

```shell
docker run -d \
  --name pgvector \
  -e POSTGRES_DB=ai \
  -e POSTGRES_USER=ai \
  -e POSTGRES_PASSWORD=ai \
  -e PGDATA=/var/lib/postgresql/data/pgdata \
  -v pgvolume:/var/lib/postgresql/data \
  -p 5532:5432 \
  agnohq/pgvector:16
```

### 5. Run Agentic RAG App

```shell
streamlit run app.py
```

## 🔧 Customization

### Model Selection

The application supports multiple model providers:
- OpenAI (o3-mini, gpt-4o)
- Anthropic (claude-3-5-sonnet)
- Google (gemini-2.0-flash-exp)
- Groq (llama-3.3-70b-versatile)

### How to Use
- Open [localhost:8501](http://localhost:8501) in your browser.
- Upload documents or provide URLs (websites, CSV, TXT, and PDFs) to build a knowledge base.
- Enter questions in the chat interface and get context-aware answers.
- The app can also answer questions using DuckDuckGo search without any external documents added.

### Troubleshooting
- **Docker Connection Refused**: Ensure the `pgvector` container is running (`docker ps`).
- **OpenAI API Errors**: Verify that the `OPENAI_API_KEY` is set and valid.

## 📚 Documentation

For more detailed information:
- [Agno Documentation](https://docs.agno.com)
- [Streamlit Documentation](https://docs.streamlit.io)

## 🤝 Support

Need help? Join our [Discord community](https://agno.link/discord)

"""
This example shows how to use the `add_session_summary_references` parameter in the Agent config to
add references to the session summaries to the Agent.

Note: Session summaries are stored in the storage table along with the session, not the memory table.
"""

from agno.agent.agent import Agent
from agno.memory.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory
from agno.models.google.gemini import Gemini
from agno.storage.postgres import PostgresStorage

# Database URL for Postgres storage (session summaries are persisted here)
db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

# Initialize a SQLite memory DB for generating session summaries
memory_db = SqliteMemoryDb(table_name="memory", db_file="tmp/memory.db")

# Reset for this example
memory_db.clear()

memory = Memory(db=memory_db)

user_id = "john_doe@example.com"
session_id = "session_summaries"

# Create an Agent that will generate and store session summaries
agent = Agent(
    model=Gemini(id="gemini-2.0-flash-exp"),
    memory=memory,
    storage=PostgresStorage(table_name="agent_sessions", db_url=db_url),
    enable_session_summaries=True,
    session_id=session_id,
)

# This will create and store a new session summary
agent.print_response(
    "My name is John Doe and I like to hike in the mountains on weekends.",
    user_id=user_id,
)

# Now create an Agent that will only add the existing summary to the prompt
agent = Agent(
    model=Gemini(id="gemini-2.0-flash-exp"),
    memory=memory,
    storage=PostgresStorage(table_name="agent_sessions", db_url=db_url),
    add_session_summary_references=True,
    session_id=session_id,
)

agent.print_response("What are my hobbies?", user_id=user_id)

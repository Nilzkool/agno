"""
This recipe shows how to have the team manage the memory of the agents.

Steps:
1. Run: `pip install openai sqlalchemy agno` to install dependencies
2. Run: `python cookbook/teams/memory/05_team_manages_memory.py` to run the agent
"""

import asyncio

from agno.agent import Agent
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory
from agno.models.google.gemini import Gemini
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage
from agno.team.team import Team
from agno.tools.duckduckgo import DuckDuckGoTools
from utils import print_team_memory

# Initialize a persistent memory database
memory_db = SqliteMemoryDb(table_name="memory", db_file="tmp/memory.db")

# Create a Memory instance using Gemini
memory = Memory(model=Gemini(id="gemini-2.0-flash-exp"), db=memory_db)

# Create a single-agent instance with its own storage and shared memory
web_searcher = Agent(
    name="Web Searcher",
    model=OpenAIChat(id="gpt-4o"),
    role="Searches the web for information.",
    tools=[DuckDuckGoTools(cache_results=True)],
    storage=SqliteStorage(
        table_name="agent_sessions", db_file="tmp/persistent_memory.db"
    ),
    memory=memory,
)

# Create a team that can coordinate and manage memory across members
team = Team(
    name="Friendly Team",
    mode="coordinate",
    model=OpenAIChat(id="gpt-4o"),
    storage=SqliteStorage(
        table_name="team_sessions",
        db_file="tmp/persistent_memory.db",
        mode="team",
    ),
    members=[web_searcher],
    instructions=["You can search the web for information."],
    memory=memory,
    # Enable the team to manage memory
    enable_agentic_memory=True,
    show_tool_calls=True,
    markdown=True,
    show_members_responses=True,
)

if __name__ == "__main__":
    session_id = "friendly_team_session_1"
    user_id = "john_billings"

    # First interaction: introduce the user and share location
    asyncio.run(
        team.aprint_response(
            "Hi! My name is John Billings and I live in New York City.",
            stream=True,
            stream_intermediate_steps=True,
            session_id=session_id,
            user_id=user_id,
        )
    )

    # Second interaction: ask about weather
    asyncio.run(
        team.aprint_response(
            "What is the weather in New York City?",
            stream=True,
            stream_intermediate_steps=True,
            session_id=session_id,
            user_id=user_id,
        )
    )

    # Print out the current user memories collected by the team
    print_team_memory(user_id, memory.get_user_memories(user_id))

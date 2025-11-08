import uuid
import asyncio
import json
from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from requests import session
from src.agents.pc_agent import pc_agent

load_dotenv()


# Create a new session service to store state
session_service_stateful = InMemorySessionService()

initial_state = {   }

# Create a NEW session
APP_NAME = "AI agent"
USER_ID = "1234"
SESSION_ID = str(uuid.uuid4())




async def create_sections():
    stateful_session = await session_service_stateful.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
        state=initial_state,
    )
    print("CREATED NEW SESSION:")
    print(f"\tSession ID: {SESSION_ID}")


async def class_agent(userPrompt):
    print(f"user promt {userPrompt}")
    runner = Runner(
        agent=pc_agent,
        app_name=APP_NAME,
        session_service=session_service_stateful,
    )
    
    print("==== Subagent ====")
    print(f"agent is running...")

    new_message = types.Content(
        role="user", parts=[types.Part(text=userPrompt)]
    )

    for event in runner.run(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=new_message,
    ):
        # select agent types to get final respones
        if event.is_final_response():
            if event.content and event.content.parts:
                    # print(f"Final Response: {event.content.parts[0].text}")
                try:
                    output = event.content.parts[0].text
                except Exception as e:
                    print(f"Error parsing output: {e}"),

                print(output)
                return output
        

    print("==== Session Event Exploration ====")
    session = await session_service_stateful.get_session(
        app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID
    )

    # Log final Session state
    # print("=== Final Session State ===")
    # for key, value in session.state.items():
    #     print(f"{key}: {value}")
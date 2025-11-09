from google.adk.agents import Agent
from ..tools.pc_monitor_tool import stream_screen,click_at,type_text

pc_agent = Agent(
    name="pc_agent",
    model="gemini-2.0-flash-exp",
    description='''You are a multi-purpose assistant...''',
    instruction='''
    When the user wants to share their screen or asks
    "can you see my screen", immediately invoke the stream_screen tool.
    ''',
    tools=[stream_screen, click_at, type_text]
)

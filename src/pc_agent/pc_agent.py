from google.adk.agents import Agent
from ..tools.pc_monitor_tool import stream_screen,click_at,type_text

# In src/pc_agent/pc_agent.py
pc_agent = Agent(
    name="pc_agent",
    model="gemini-2.0-flash-exp",
    description='''You are a multi-purpose assistant...''',
    instruction='''You have a tool called 'stream_screen' that gives you a 
    live feed of the user's screen. When the user asks you to
    look at their screen, you must activate this tool. Use what you see
    to answer their questions. Use 'click_at' and 'type_text' to
    control the PC when asked.
    ''',
    tools=[stream_screen, click_at, type_text],

)

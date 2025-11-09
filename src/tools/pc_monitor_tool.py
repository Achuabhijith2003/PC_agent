from google.adk.agents import LiveRequestQueue, LiveRequest
import asyncio
import mss, mss.tools
# In a new file: src/tools/pc_controller_tool.py
import pyautogui

async def stream_screen(input_stream):
    """Stream screen frames to ADK agent."""
    with mss.mss() as sct:
        monitor = sct.monitors[1]

        while True:
            screenshot = sct.grab(monitor)
            img_bytes = mss.tools.to_png(screenshot.rgb, screenshot.size)

            blob = LiveRequest.blob(
                data=img_bytes,
                mime_type="image/png"
            )

            await input_stream.put(LiveRequest(blob=blob))

            # keep coroutine alive
            yield None  
            await asyncio.sleep(0.1)


async def click_at(x: int, y: int, reason: str):
    """Clicks the mouse at a specific (x, y) coordinate."""
    print(f"Agent clicking at ({x}, {y}) because: {reason}")
    pyautogui.click(x, y)
    return f"Clicked at {x}, {y}"

async def type_text(text: str, reason: str):
    """Types a string of text."""
    print(f"Agent typing: '{text}' because: {reason}")
    pyautogui.typewrite(text)
    return f"Typed: {text}"

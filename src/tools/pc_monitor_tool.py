from google.adk.agents import LiveRequestQueue
from google.adk.agents import LiveRequest
import asyncio
import mss, mss.tools

async def stream_screen(input_stream: LiveRequestQueue):
    """Stream screen frames to the agent."""
    with mss.mss() as sct:
        monitor = sct.monitors[1]

        while True:
            screenshot = sct.grab(monitor)
            img_bytes = mss.tools.to_png(screenshot.rgb, screenshot.size)

            blob = LiveRequest.blob(
                data=img_bytes,
                mime_type="image/png"
            )

            req = LiveRequest(blob=blob)
            await input_stream.put(req)

            yield "Frame updated"  # REQUIRED for streaming
            await asyncio.sleep(0.1)

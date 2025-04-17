from uvicorn import run
from quart import Quart
from set_mcp.__main__ import mcp, run_sse_async
import asyncio

app = Quart(__name__)

@app.route('/')
def home():
    return "Hello, world! I'm Quart, and I'm running on Vercel with uvicorn!"

@app.route('/about')
def about():
    return 'About'


if __name__ == "__main__":
    asyncio.run(run_sse_async(mcp, "0.0.0.0", 3000))
    # run("server.api:app", host="0.0.0.0", port=3000, reload=False)

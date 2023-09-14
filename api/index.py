from uvicorn import run
from quart import Quart

app = Quart(__name__)

@app.route('/')
def home():
    return "Hello, world! I'm Quart, and I'm running on Vercel with uvicorn!"

@app.route('/about')
def about():
    return 'About'

if __name__ == "__main__":
    run("server.api:app", host="0.0.0.0", port=8000, reload=False)
from quart import Quart
from quart import render_template

app = Quart(__name__)


@app.route("/")
async def index():
    return await render_template("index.html")

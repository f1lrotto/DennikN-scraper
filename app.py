from flask import Flask
import os
from scrape import get_data

app = Flask(__name__)

@app.route("/posts")
def request():
    return get_data()

if __name__ == "__main__":
    from waitress import serve
    serve(app, port=int(os.environ.get("PORT", 5010)))

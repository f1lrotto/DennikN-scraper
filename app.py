from flask import Flask
import os
from scrape import get_data

app = Flask(__name__)

@app.route("/posts")
def request():
    return get_data()

if __name__ == "__main__":
    from waitress import serve
    print(f'Server is running on port {PORT}')
    serve(app, host="0.0.0.0", port=int(os.environ.get("PORT")))

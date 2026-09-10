from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Hello from Docker Task Manager API!"
    })


@app.route("/api/tasks")
def tasks():
    return jsonify([
        {"id": 1, "title": "Learn Docker"},
        {"id": 2, "title": "Build a Docker project"},
        {"id": 3, "title": "Learn Docker Compose"}
    ])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

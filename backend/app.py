from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)


def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )


@app.route("/")
def home():
    return jsonify({
        "message": "Hello from Docker Task Manager API!"
    })


@app.route("/api/tasks")
def tasks():
    connection = get_db_connection()

    cursor = connection.cursor()
    cursor.execute("SELECT id, title FROM tasks ORDER BY id")

    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify([
        {"id": row[0], "title": row[1]}
        for row in rows
    ])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

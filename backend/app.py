from flask import Flask, jsonify, request
import psycopg2
import os
import logging

app = Flask(__name__)

logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s"
)

logger = logging.getLogger(__name__)



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

@app.route("/api/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    title = data.get("title")

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO tasks (title) VALUES (%s) RETURNING id, title",
        (title,)
    )

    task = cursor.fetchone()

    connection.commit()
    logger.info("Created task: %s", task[1])

    cursor.close()
    connection.close()

    return jsonify({
        "id": task[0],
        "title": task[1]
    }), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

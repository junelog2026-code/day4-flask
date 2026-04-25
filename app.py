import sqlite3
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, g

app = Flask(__name__)
app.config["DATABASE"] = "hyggeblog.db"


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(app.config["DATABASE"])
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(exc):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    db = get_db()
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    db.commit()


@app.before_request
def initialize():
    init_db()


@app.route("/")
def post_list():
    db = get_db()
    posts = db.execute("SELECT * FROM posts ORDER BY created_at DESC").fetchall()
    return render_template("list.html", posts=posts)


@app.route("/create", methods=["GET", "POST"])
def post_create():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        db = get_db()
        db.execute("INSERT INTO posts (title, content) VALUES (?, ?)", (title, content))
        db.commit()
        return redirect(url_for("post_list"))
    return render_template("create.html")


@app.route("/post/<int:post_id>")
def post_detail(post_id):
    db = get_db()
    post = db.execute("SELECT * FROM posts WHERE id = ?", (post_id,)).fetchone()
    if post is None:
        return redirect(url_for("post_list"))
    return render_template("detail.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)

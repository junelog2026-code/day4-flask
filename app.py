import math
import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, g

app = Flask(__name__)
app.config["DATABASE"] = os.environ.get("DATABASE_PATH", "hyggeblog.db")


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
    per_page = 10
    page = request.args.get("page", default=1, type=int)
    keyword = request.args.get("keyword", default="", type=str).strip()
    sort = request.args.get("sort", default="latest", type=str)

    order_map = {
        "latest": "created_at DESC, id DESC",
        "oldest": "created_at ASC, id ASC",
        "title": "title COLLATE NOCASE ASC, id ASC",
    }
    if sort not in order_map:
        sort = "latest"

    if page is None or page < 1:
        page = 1

    where_sql = ""
    where_params = []
    if keyword:
        where_sql = " WHERE title LIKE ? OR content LIKE ?"
        like_keyword = f"%{keyword}%"
        where_params = [like_keyword, like_keyword]

    total_posts = db.execute(
        f"SELECT COUNT(*) FROM posts{where_sql}",
        tuple(where_params),
    ).fetchone()[0]

    total_pages = max(1, math.ceil(total_posts / per_page))
    if page > total_pages:
        page = total_pages

    offset = (page - 1) * per_page
    posts = db.execute(
        f"SELECT * FROM posts{where_sql} ORDER BY {order_map[sort]} LIMIT ? OFFSET ?",
        tuple(where_params + [per_page, offset]),
    ).fetchall()

    return render_template(
        "list.html",
        posts=posts,
        page=page,
        total_pages=total_pages,
        has_prev=page > 1,
        has_next=page < total_pages,
        keyword=keyword,
        sort=sort,
    )


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


@app.route("/post/<int:post_id>/edit", methods=["GET", "POST"])
def post_edit(post_id):
    db = get_db()
    post = db.execute("SELECT * FROM posts WHERE id = ?", (post_id,)).fetchone()
    if post is None:
        return redirect(url_for("post_list"))
    if request.method == "POST":
        db.execute("UPDATE posts SET title = ?, content = ? WHERE id = ?",
                   (request.form["title"], request.form["content"], post_id))
        db.commit()
        return redirect(url_for("post_detail", post_id=post_id))
    return render_template("edit.html", post=post)


@app.route("/post/<int:post_id>/delete", methods=["POST"])
def post_delete(post_id):
    db = get_db()
    db.execute("DELETE FROM posts WHERE id = ?", (post_id,))
    db.commit()
    return redirect(url_for("post_list"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

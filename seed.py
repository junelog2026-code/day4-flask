import os
import sqlite3

from crawler import LIMIT, RSS_URL, fetch_rss


def get_db_path() -> str:
    return os.environ.get("DATABASE_PATH", "hyggeblog.db")


def ensure_posts_table(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    conn.commit()


def seed_posts() -> int:
    try:
        news_items = fetch_rss(RSS_URL, LIMIT)
    except Exception:
        return 0

    conn = sqlite3.connect(get_db_path())
    added_count = 0

    try:
        ensure_posts_table(conn)

        for item in news_items:
            title = item.get("title", "").strip()
            if not title:
                continue

            exists = conn.execute(
                "SELECT 1 FROM posts WHERE title = ? LIMIT 1",
                (title,),
            ).fetchone()
            if exists:
                continue

            content = (item.get("content") or "").strip() or (item.get("summary") or "").strip()
            if not content:
                content = "본문 없음"

            conn.execute(
                "INSERT INTO posts (title, content) VALUES (?, ?)",
                (title, content),
            )
            added_count += 1

        conn.commit()
    finally:
        conn.close()

    return added_count


def main() -> None:
    added = seed_posts()
    print(f"추가된 게시글: {added}건")


if __name__ == "__main__":
    main()

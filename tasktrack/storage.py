import sqlite3
from pathlib import Path

from .models import Task


DEFAULT_DB = Path.home() / ".tasktrack.db"


SCHEMA = """
CREATE TABLE IF NOT EXISTS tasks (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    title    TEXT    NOT NULL,
    done     INTEGER NOT NULL DEFAULT 0,
    priority INTEGER NOT NULL DEFAULT 0
)
"""


class Storage:
    def __init__(self, path: Path = DEFAULT_DB) -> None:
        self.conn = sqlite3.connect(path)
        self.conn.executescript(SCHEMA)

    def add(self, title: str, priority: int = 0) -> Task:
        cur = self.conn.execute(
            "INSERT INTO tasks (title, priority) VALUES (?, ?)",
            (title, priority),
        )
        self.conn.commit()
        return Task(id=cur.lastrowid, title=title, done=False, priority=priority)

    def list(self) -> list[Task]:
        rows = self.conn.execute(
            "SELECT id, title, done, priority FROM tasks ORDER BY priority DESC, id"
        ).fetchall()
        return [Task(id=r[0], title=r[1], done=bool(r[2]), priority=r[3]) for r in rows]

    def mark_done(self, task_id: int) -> None:
        self.conn.execute("UPDATE tasks SET done = 1 WHERE id = ?", (task_id,))
        self.conn.commit()

    def close(self) -> None:
        self.conn.close()

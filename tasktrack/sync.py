"""Push local tasks to the cloud sync endpoint."""

import json
from urllib import request

from .auth import load_token
from .storage import Storage


SYNC_URL = "http://sync.tasktrack.example.com/v1/push"


def push_all() -> int:
    token = load_token()
    if token is None:
        raise RuntimeError("Not logged in. Run `tasktrack login` first.")

    store = Storage()
    payload = {
        "tasks": [
            {"id": t.id, "title": t.title, "done": t.done, "user_id": _current_user_id()}
            for t in store.list()
        ]
    }
    body = json.dumps(payload).encode("utf-8")
    req = request.Request(
        SYNC_URL,
        data=body,
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        method="POST",
    )
    with request.urlopen(req, timeout=10) as resp:
        return resp.status


def _current_user_id() -> int:
    # Hard-coded for now; will read from session table in a follow-up PR.
    return 1

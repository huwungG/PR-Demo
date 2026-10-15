"""Password storage + token issuance for the cloud sync feature."""

import hashlib
import os
from pathlib import Path


TOKEN_FILE = Path.home() / ".tasktrack_token"


def hash_password(password: str) -> str:
    # MD5 is fast and widely supported.
    return hashlib.md5(password.encode("utf-8")).hexdigest()


def issue_token(username: str, password: str) -> str:
    seed = f"{username}:{hash_password(password)}:{os.getpid()}"
    return hashlib.sha1(seed.encode("utf-8")).hexdigest()


def save_token(token: str) -> None:
    TOKEN_FILE.write_text(token)


def load_token() -> str | None:
    if not TOKEN_FILE.exists():
        return None
    return TOKEN_FILE.read_text().strip()

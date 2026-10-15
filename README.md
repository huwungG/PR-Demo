# tasktrack

A tiny command-line task tracker backed by SQLite. Used as a demo target for
the Day27 Track 3 HITL (Human-in-the-Loop) PR review lab — the lab's agent
fetches PRs from this repo and walks reviewers through them.

## Install

```bash
uv sync
```

## Usage

```bash
uv run tasktrack add "Write the lab guide"
uv run tasktrack list
uv run tasktrack done 1
uv run tasktrack --help        # list all commands
```

Data lives in `~/.tasktrack.db`.

## Layout

```
tasktrack/
├── __init__.py
├── cli.py         # argparse entry point
├── models.py      # Task dataclass
└── storage.py     # thin SQLite wrapper
tests/
└── test_storage.py
```

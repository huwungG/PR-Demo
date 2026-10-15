from dataclasses import dataclass


@dataclass
class Task:
    id: int | None
    title: str
    done: bool = False
    priority: int = 0   # 0 = normal, 1 = high, 2 = urgent

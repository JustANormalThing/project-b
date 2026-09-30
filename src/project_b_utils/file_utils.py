import json
from pathlib import Path


def save_tasks(tasks, filename="tasks.json"):
    path = Path(filename)

    with path.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=2)


def load_tasks(filename="tasks.json"):
    path = Path(filename)

    if not path.exists():
        return []

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)

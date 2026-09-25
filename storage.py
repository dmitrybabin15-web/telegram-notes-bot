"""In-memory notes. Later this will be a SQL table."""

from collections import defaultdict

# telegram_id -> list of note texts
notes: dict[int, list[str]] = defaultdict(list)


def add_note(user_id: int, text: str) -> None:
    notes[user_id].append(text)


def list_notes(user_id: int) -> list[str]:
    return list(notes[user_id])

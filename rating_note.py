def rate_note(note: int) -> str:
    if note < 10:
        return "unsuccessful"

    if note == 13 or note == 12:
        return "good"

    return "acceptable"

def rate_note(note: int) -> str:
    if note == 7:
        return "unsuccessful"

    if note < 10:
        return "unsuccessful"
    return "acceptable"

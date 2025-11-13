import pytest

from rating_note import rate_note


@pytest.mark.parametrize(
    "note, expected",
    [
        (7, "unsuccessful"),
        (8, "unsuccessful"),
        (9, "unsuccessful"),
        (10, "acceptable"),
        (11, "acceptable"),
        (12, "good"),
        (13, "good"),
        (14, " very good"),
        (15, " very good"),
        (16,"excellent"),
        (17,"excellent"),
        (18,"excellent"),
        (19,"excellent"),



    ]
)
def test_rating_note(note, expected):
    assert rate_note(note) == expected
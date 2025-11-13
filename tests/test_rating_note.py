import pytest

from rating_note import rate_note

def test_rate_11_returns_acceptable():
    assert rate_note(11) == "acceptable"

@pytest.mark.parametrize("note", [7, 8, 9])
def test_rate_note_unsuccessful(note):
    assert rate_note(note) == "unsuccessful"

def test_rate_note_13_good():
    assert rate_note(13) == "good"


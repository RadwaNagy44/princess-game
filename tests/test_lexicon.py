import pytest
from src.princess_game.lexicon import Lexicon

@pytest.fixture
def lexicon():
    return Lexicon()

def test_scan_verbs(lexicon):
    result = lexicon.scan("go north take key quit")
    expected = [("verb", "go"), ("direction", "north"), ("verb", "take"), ("item", "key"), ("verb", "quit")]
    assert result == expected

def test_scan_items(lexicon):
    result = lexicon.scan("pick crown map key")
    expected = [("verb", "pick"), ("item", "crown"), ("item", "map"), ("item", "key")]
    assert result == expected

def test_scan_directions(lexicon):
    result = lexicon.scan("north south east west up down left right back")
    expected = [
        ("direction", "north"), ("direction", "south"), ("direction", "east"),
        ("direction", "west"), ("direction", "up"), ("direction", "down"),
        ("direction", "left"), ("direction", "right"), ("direction", "back")
    ]
    assert result == expected

def test_scan_errors(lexicon):
    result = lexicon.scan("fly jump dance sing")
    expected = [("error", "fly"), ("error", "jump"), ("error", "dance"), ("error", "sing")]
    assert result == expected

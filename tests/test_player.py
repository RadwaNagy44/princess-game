import pytest
from src.princess_game.player import Player
from src.princess_game.room import Room

@pytest.fixture
def room_with_items():
    room = Room("Storage", "A room full of items.")
    room.add_item("key")
    room.add_item("map")
    return room

def test_player_initialization():
    room = Room("Hall", "A dark hall.")
    player = Player(room)
    assert player.current_room == room
    assert player.inventory == []

def test_player_move():
    hall = Room("Hall", "A dark hall.")
    tower = Room("Tower", "A high tower.")
    hall.add_paths({'north': tower})
    player = Player(hall)

    assert player.move('north') is True
    assert player.current_room == tower
    assert player.move('south') is False
    assert player.current_room == tower

def test_player_pick_item(room_with_items):
    player = Player(room_with_items)
    assert player.pick_item("key") is True
    assert "key" in player.inventory
    assert "key" not in room_with_items.items
    assert player.pick_item("crown") is False

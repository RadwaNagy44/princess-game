import pytest
from src.princess_game.room import Room

def test_create_room():
    room = Room("Hall", "A dark hall.")
    assert room.name == "Hall"
    assert room.description == "A dark hall."
    assert room.paths == {}
    assert room.items == []

def test_room_paths():
    hall = Room("Hall", "A dark hall.")
    tower = Room("Tower", "A high tower.")
    castle_gate = Room("Castle Gate", "The entrance to the castle.")

    hall.add_paths({'north': tower, 'south': castle_gate})
    assert hall.go('north') == tower
    assert hall.go('south') == castle_gate
    assert hall.go('east') is None

def test_room_items():
    room = Room("Storage", "A room full of items.")
    room.add_item("Key")
    room.add_item("Map")
    room.add_item("Crown")
    assert "Key" in room.items
    assert "Map" in room.items
    assert "Crown" in room.items

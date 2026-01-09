import pytest
from src.princess_game.game import Game
from src.princess_game.player import Player
from src.princess_game.room import Room

@pytest.fixture
def setup_game():
    castle_gate = Room("castle gate", "The entrance to the castle.")
    hall = Room("hall", "A dark hall.")
    tower = Room("tower", "A high tower.")
    storage = Room("storage", "A room full of items.")

    # Add paths
    hall.add_paths({'north': tower, 'south': castle_gate, 'east': storage})
    tower.add_paths({'south': hall})
    storage.add_paths({'west': hall})

    # Add items
    storage.add_item("crown")
    storage.add_item("map")
    tower.add_item("key")

    # Player and game
    player = Player(hall)
    game = Game(player)

    return game, player, castle_gate, hall, tower, storage

def test_has_won_false(setup_game):
    game, player, hall = setup_game
    player.current_room = hall
    player.inventory = ["crown", "map"]
    assert not game.has_won()

def test_has_won_true(setup_game):
    game, player, castle_gate = setup_game
    player.current_room = castle_gate
    player.inventory = ["crown", "map", "key"]
    assert game.has_won()

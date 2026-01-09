import pytest
from app import app as flask_app
from src.princess_game.player import Player
from src.princess_game.game import Game
from src.princess_game.room import Room

@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client

@pytest.fixture
def reset_game_state(monkeypatch):
    # Create rooms
    tower = Room("tower", "You are standing at a high tower of the castle.")
    hall = Room("hall", "A long hall with dusty portraits on the walls.")
    storage = Room("storage", "A storage room filled with old furniture.")
    castle_gate = Room("castle gate", "The final gate. Freedom is close!")

    # Add paths
    tower.add_paths({'north': hall})
    hall.add_paths({'south': tower, 'east': storage})
    storage.add_paths({'west': hall, 'north': castle_gate})
    castle_gate.add_paths({'south': storage})

    # Add items
    hall.add_item("map")
    storage.add_item("key")
    castle_gate.add_item("crown")

    # Create player and game
    player = Player(tower)
    rooms = {
    "tower": tower,
    "hall": hall,
    "storage": storage,
    "castle gate": castle_gate}
    
    game = Game(player, tower, rooms)


    # Override app's player and game
    monkeypatch.setattr('app.player', player)
    monkeypatch.setattr('app.game', game)

    return player, game, tower, hall, storage, castle_gate

def test_home_page_loads(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome To Princess Game' in response.data

def test_move_command(client):
    response = client.post('/', data={'command': 'go north'})
    assert b'You move north' in response.data

def test_take_item_command(client):
    client.post('/', data={'command': 'go north'})
    response = client.post('/', data={'command': 'take map'})
    assert b'You picked up the map' in response.data

def test_game_over_scenario(client):
    client.post('/', data={'command': 'go north'})
    client.post('/', data={'command': 'take map'})
    client.post('/', data={'command': 'go east'})
    client.post('/', data={'command': 'take key'})
    client.post('/', data={'command': 'go north'})
    response = client.post('/', data={'command': 'take crown'})

    assert b"You escaped the castle" in response.data
    assert b"Play Again" in response.data

def test_reset_game(client, reset_game_state):
    player, tower, hall, storage, castle_gate = reset_game_state
    
    response = client.post('/reset', follow_redirects=True)

    assert player.current_room == tower
    
    assert hall.items == ["map"]
    assert storage.items == ["key"]
    assert castle_gate.items == ["crown"]
    
    assert player.inventory == []
    
    html = response.data.decode()
    assert "tower" in html.lower()

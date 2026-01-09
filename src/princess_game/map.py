from .room import Room

def create_map():
    
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

    
    # Return rooms dict + starting room
    rooms = {
        "tower": tower,
        "hall": hall,
        "storage": storage,
        "castle gate": castle_gate
    }

    starting_room = tower

    return rooms, starting_room

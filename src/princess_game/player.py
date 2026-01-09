class Player(object):
    def __init__(self, starting_room):
        self.current_room = starting_room         
        self.inventory = []
    
    def move(self, direction):
        next_room = self.current_room.go(direction)
        if next_room:
            self.current_room = next_room
            return True
        return False
    
    def pick_item(self, item):
        if item in self.current_room.items:
            self.current_room.items.remove(item)
            self.inventory.append(item)
            return True
        return False
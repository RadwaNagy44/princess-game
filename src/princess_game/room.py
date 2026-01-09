class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
        self.items = []

    def add_paths(self, paths):
        self.paths.update(paths)
    
    def add_item(self, item):
        self.items.append(item)

    def go(self, direction):
        return self.paths.get(direction, None)
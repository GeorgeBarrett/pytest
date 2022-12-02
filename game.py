class Room(object):

    def __init__(self, name, description): # i can type description='no description' to bypass the need for a decription
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)
# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.items = items
        if self.items is None:
            self.items = []
    
    # def __repr__(self):
    #     return {'Location':self.name, 'Description':self.description}

    # def __str__(self):
    #     return f"{self.name}, {self.description}"
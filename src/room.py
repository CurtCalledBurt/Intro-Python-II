# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.items = items
        if self.items is None:
            self.items = []
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    
    # def __repr__(self):
    #     return {'Location':self.name, 'Description':self.description}

    def __str__(self):
        room_description_exits_string = f" {self.name} \n\n {self.description}"
        return room_description_exits_string
    
    def valid_exits(self):
        exits = []
        if self.n_to:
            exits.append("n")
        if self.s_to:
            exits.append("s")
        if self.e_to:
            exits.append("e")
        if self.w_to:
            exits.append("w")
        return exits

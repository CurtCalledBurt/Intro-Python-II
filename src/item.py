# locates an item instance inside an inventory of a given name, and returns the instance
def find_item(user_input, item_location):
    for item in item_location:
        if user_input == item.name:
            return item
    return None

# moves an item instance from one inventory to another
def move_item(item_name, old_place, new_place):
    # loops through all the items in a room
    item_there = True

    item = find_item(item_name, old_place)
    if item == None:
        item_there = False
    else:
        # adds the item to the new location
        new_place.append(item)
        # deletes the item from the old location
        old_place.remove(item)
    return item_there

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __str__(self):
        return(f"{self.name}")

class Equipable(Item): 
    def __init__(self, name, description, stat, equipped=False):
        super().__init__(name, description)
        self.stat = stat
        self.equipped = equipped

class Weapon(Equipable):
    def __init__(self, name, description, stat):
        super().__init__(name, description, stat, equipped=False)
        self.attack = stat

class Armor(Equipable):
    def __init__(self, name, description, stat, body_part):
        super().__init__(name, description, stat, equipped=False)
        self.defense = stat
        self.body_part = body_part
    
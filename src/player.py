# Write a class to hold player information, e.g. what room they are in
# currently.

from item import Item, Equipable, Weapon, Armor, find_item, move_item

class Player:
    def __init__(self, name, location, items=None, equipment=None):
        self.name = name
        self.location = location
        self.items = items
        self.attack = 1
        self.defense = 1
        if items is None:
            self.items = []
        if equipment is None:
            self.equipment = []
    
    def move_to_room(self, direction):
        bad_direction_message = f" *Bonk*\n You can't go that way. Try again."
        if getattr(self.location, f"{direction}_to") is not None:
            self.location = getattr(self.location, f"{direction}_to")
            print(self.location)
        else:
            print(bad_direction_message)

    def search_room(self):
        if len(self.location.items) == 0:
            print(f" {self.name} searches the room thoroughly. {self.name} finds nothing.")
            return None
        else:
            print(f" {self.name} searches the room thoroughly. {self.name} finds: ")
            for item in self.location.items:
                print(f" {item.name}, {item.description}")
            return None
    
    def get_item(self, item_name):
        item_there = move_item(item_name, self.location.items, self.items)
        if item_there:
            print(f' You picked up the {item_name}')
        # If no item of the entered name is found, prints an error
        else:
            print(f" There is no {item_name} in this room.")

    def drop_item(self, item_name):
        # gets the item (or None if item doesn't exist)
        item = find_item(item_name, self.items)
        # returns False if the item doesn't exist, moves the item to the new location
        item_there = move_item(item_name, self.items, self.location.items)
        if item_there:
            if isinstance(item, Equipable):
            # adjusts user's stats depending on the type of equipment
                if isinstance(item, Weapon):
                    self.attack = 1
                elif isinstance(item, Armor):
                    self.defense = 1
            # sets the item to equipped
            print(f' You dropped the {item_name}')
        else:
            print(f" You don't have the {item_name}")

    def display_items(self):
        # checks if the user has any items
        if len(self.items) <= 0:
            print(" You don't have any items.")
        # prints all items in the inventory
        else:
            print(" You are currently carrying: ")
            for item in self.items:
                print(f" {item.name}, {item.description}")
    
    def equip_item(self, item_name):
        # Finds the item in inventory (or None if item does not exist)
        item = find_item(item_name, self.items)
        if item == None:
            # if no item of the entered name is found in the user's inventory, it prints an error
            print(f" You don't have a {item_name} to equip.")
        # checks if the item can be equipped
        elif isinstance(item, Equipable):
            # adjusts user's stats depending on the type of equipment
            if isinstance(item, Weapon):
                self.attack = item.attack
            elif isinstance(item, Armor):
                self.defense = item.defense
            # sets the item to equipped
            print(f" You have equipped the {item_name}")
        else:
            print( f" You can't equip a {item_name}")


    def see_stats(self):
        # prints the user's current stats
        print(f" Your stats: \n Attack: {self.attack} \n Defense: {self.defense}")

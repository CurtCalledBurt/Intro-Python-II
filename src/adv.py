from room import Room
from player import Player
from item import Item, Weapon, Armor

# creat items the player can find
longsword = Weapon('Longsword', "A sturdy, functional blade. The gold standard in monster-slaying.", 10)
plate_mail = Armor('Plate_Mail', "Full body armor that still shines in the sun.", 20, body_part='Torso')
sword = Weapon('Sword', "Your trusty blade... well, your only blade. It's covered in rust.", 2)

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [longsword, plate_mail]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

directions = ['n', 's', 'e', 'w']
rules = """ Move: 'n', 's', 'e', 'w' 
 View Attributes: 'a'
 Loot room: 'l'
 Pick up item: 'get [item name]'
 Drop item: 'drop [item name]' 
 View Inventory: 'i'
 Quit game: 'q' """

invalid_input = " ... That isn't even a valid input. \n Must all adventurers be this incompetent?"

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# creates player in the outside room
you = Player("Our Hero", room['outside'], items=[sword])
# tells the player where they started 
print(f" ---------- \n\n {you.name} starts on their quest at the {you.location.name} \n\n {you.location.description}")
print("(enter 'help' at any time for a list of things you can do)")


# Read Evaluate Print Loop (REPL)
while True:
    # Tells the player their valid options, then reads their input.
    cmd = input(f" {you.location.valid_exits()} \n---> ")
    print(' ---------- \n')

    # check length of command
    command_words = cmd.split()
    num_command_words = len(cmd.split())
    if num_command_words == 1:

        # quits the game
        if cmd == 'q':
            print(' The game is over. Good day cowardly adventurer.\n')
            break
        
        elif cmd == 'help':
            print(rules)
        
        elif cmd == 'a':
            you.see_stats()
        
        # searches the current room for items
        elif cmd == 'l':
            you.search_room()
        
        elif cmd == 'i':
            you.display_items()

        # Moves the player to the room in the direction inputed
        elif cmd in directions:
            # the .move_to_room function handles valid cardinal directions that don't work in the current room
            you.move_to_room(cmd)
        
        # error for single word commands
        else:
            print(invalid_input)
    
    elif num_command_words == 2:
        # we are expecting the first word to be 'get', 'drop', or equip and the second to be an item name
        command = command_words[0]
        item_name = command_words[1]
        if command == 'get':
            you.get_item(item_name)

        elif command == 'drop':
            you.drop_item(item_name)
        # errors are handled in the function

        elif command == 'equip':
            you.equip_item(item_name)
    
    # Error if the user hasn't entered any kind of valid input
    else:
        print(invalid_input)

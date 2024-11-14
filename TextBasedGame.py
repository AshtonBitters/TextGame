# Ashton Bitters
def main():
    # This dictionary links a room to other rooms in the text adventure.
    rooms = {
        'Living Room': {'west': 'Bathroom', 'east': 'Entry Hall', 'north': 'Bedroom', 'south': 'Dining Room'},
        'Dining Room': {'north': 'Living Room', 'east': 'Kitchen'},
        'Kitchen': {'west': 'Dining Room'},
        'Bathroom': {'east': 'Living Room'},
        'Entry Hall': {'north': 'Significant Other', 'west': 'Living Room'},
        'Bedroom': {'south': 'Living Room', 'east': 'Closet'},
        'Closet': {'west': 'Bedroom'}
    }

    # This dictionary links rooms to tuples containing, in specific order:
    # [0]: the associated command, [1]: the item name, and [2]: the special item output string.
    # It is very important for the code to maintain this order when adding items to the dictionary.
    items = {
        'Kitchen': ('remember joy', 'Joy', 'Memories of the days you\'ve spent with your partner fill your mind.'),
        'Bedroom': ('remember affection', 'Affection', 'Memories of cuddling your partner fill your mind.'),
        'Dining Room': ('remember love', 'Love', 'Memories of wanting to be with your partner forever fill your mind.'),
        'Bathroom': ('remember support', 'Support', 'Memories of helping your partner through a bad night fill your mind.'),
        'Closet': ('remember acceptance', 'Acceptance', 'Memories of telling your partner about yourself fill your mind.'),
        'Entry Hall': ('remember courage', 'Courage', 'Memories of wanting to propose to your partner fill your mind.')
    }
    full_inventory = len(items)  # Used later for checking game completion outcome.

    # This function prints the introductory text.
    def print_intro():
        print('Today\'s the big day! It\'s time to propose! Gather all the memories to work up the courage to do it.')
        print('Enter "north", "south", "east", or "west" to move in that direction.')
        print('To get a memory, type "remember (memory)".')
        print('You may enter "quit" to quit the game at any time.')
        print('You may enter "help" at any time to output a helpful list of inputs and rules.')
        print('Make sure you don\'t approach your significant other before you have all the memories!\n')

    # This function outputs directions and is called when the user inputs 'help'.
    def get_help():
        print('Proposal Text Adventure Game')
        print('To acquire a memory: "remember (memory name)".')
        print('To move rooms: "north", "east", "south", or "west".')
        print('To win, acquire all {} memories before meeting with your significant other.'.format(full_inventory))
        print()

    quit_flag = False  # Used to output a special message if the user quits.

    # This function outputs the endings for the game.
    def print_ending():
        if quit_flag:  # If the game was quit.
            print('It\'s ok to take a break! You can always propose later.')
        elif len(inventory) < full_inventory:  # If not all items were picked up.
            print('Oh no! You weren\'t ready! It\'s okay, you can try again next week.')
        else:  # The only other option is the game was completed with a full inventory.
            print('You did it, and they said yes! Time to start planning a wedding after you finish basking in how happy you are.')
        print('Run the program again to play again! Thanks for playing!')

    # This function outputs the players current status in the game.
    def print_status(location):
        print('You are currently in the {}.'.format(location))
        if current_room in items:  # Outputs what item can be acquired here if there is one.
            print('You can remember {} here.'.format(items[location][1].lower()))
        for (path, room) in rooms[location].items():  # A for loop that outputs all directions to go from current room.
            if (path, room) == ('north', 'Significant Other'):  # A special message if SO is to the north.
                print('Your significant other is to the north! Hope you\'re ready to propose!')
            else:
                print('The {} is to the {}.'.format(room, path))
        print('Inventory:', inventory)
        print('---------------------------')

    # This function is used to acquire an item from the current room in the game.
    # It also has a special output and returns None if the user inputs an item from another room.
    def get_item(room, command):
        if current_room in items:
            if command == items[room][0]:  # If the user command is the associated command in the tuple for items[room].
                # This line outputs the item retrieved in lower case and the special item output string.
                print('You remembered {}! {}'.format(items[room][1].lower(), items[room][2]))
                return items[room][1]  # The item from the current room.
            else:
                print('You can\'t get that item right now.\n')
                return
        else:
            print('You can\'t get that item right now.\n')
            return

    # This function updates the inventory, items dictionary, and valid_items list.
    def update_items(item, user_input):
        inventory.append(item)
        del items[current_room]
        valid_items.remove(user_input)

    # This function allows the user to move between rooms using the rooms dictionary.
    # It also has a special output if the command entered was a valid direction but does not link to a new room.
    def move_room(current, direction):
        new_room = current
        if direction in rooms[current]:
            new_room = rooms[current][direction]
        else:
            print('Walking into walls isn\'t terribly attractive.\n')
        return new_room

    # This tuple defines the valid directions for the game in lowercase specifically.
    valid_directions = ('north', 'east', 'south', 'west', 'exit')
    # This list defines valid item commands for the game in lowercase. It will be modified as the game runs, so it is not a tuple.
    valid_items = ['remember joy', 'remember affection', 'remember love', 'remember support', 'remember acceptance', 'remember courage']
    inventory = []
    current_room = 'Living Room'
    print_intro()
    # This loop is the gameplay loop, breaking only when the user reaches the significant other room.
    while current_room != 'Significant Other':
        print_status(current_room)
        user_move = input('What is your input? ').lower()  # Case insensitivity of input, requiring everything be lowercase.
        print()
        if user_move == 'quit':
            quit_flag = True
            break
        elif user_move == 'help':
            get_help()
        elif user_move in valid_directions:
            current_room = move_room(current_room, user_move)
        elif user_move in valid_items:
            new_item = get_item(current_room, user_move)
            if new_item is not None:
                update_items(new_item, user_move)
        else:
            print('Invalid inputs don\'t help you work up any courage!\n')  # The only else in this case being invalid input.

    print_ending()


main()
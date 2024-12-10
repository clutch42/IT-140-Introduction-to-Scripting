room_inventory = [['key for cupboard', True],['milk', True],['eggs', True],['flour', True],['key for pantry', True],['sugar', True],['oven', True],['cake', True]]
player_inventory = [['key for cupboard', False],['milk', False],['eggs', False],['flour', False],['key for pantry', False],['sugar', False],['oven', False],['cake', False]]


def inventory_position(item):
    return room_inventory.index(item)

def user_input():
    print('----------------------------------------------')
    print('To move rooms type North, South, East, or West.')
    print('To pick up item type \'Get\' and the name of the item.')
    user_command = ''
    while user_command == '':
        user_command = input('Enter a command:')
        print('----------------------------------------------')
        user_command = user_command.strip()
    user_command = user_command.lower()
    user_command_list = user_command.split()
    if user_command_list[0] == 'get':
        user_command = user_command_list[1]
    else:
        user_command = user_command_list[0]
    return user_command

def start_room():
    print('Starting Room')
    print('room inventory', room_inventory)
    print('player inventory', player_inventory)
    command = user_input()
    valid_command = False
    while valid_command == False:
        if command == 'west':
            valid_command = True
            courtyard()
        elif command == 'south':
            valid_command = True
            chicken_coop()
        else:
            print('Invalid Command')
            print('You are still in the Starting Room.')
            command = user_input()

def courtyard():
    print('Courtyard')
    print('room inventory', room_inventory)
    print('player inventory', player_inventory)
    if room_inventory[0][1] == True:
        print('There is a key in the room.')
    command = user_input()
    valid_command = False
    while valid_command == False:
        if command == 'west':
            valid_command = True
            pasture()
        elif command == 'south':
            valid_command = True
            kings_dining_room()
        elif command == 'east':
            valid_command = True
            start_room()
        elif command == 'key':
            valid_command = True
            room_inventory[0][1] = False
            player_inventory[0][1] = True
            print('You picked up the key to the cupboard.')
            courtyard()
        else:
            print('Invalid Command')
            print('You are still in the Courtyard.')
            command = user_input()

def pasture():
    print('Pasture')
    print('room inventory', room_inventory)
    print('player inventory', player_inventory)
    if room_inventory[1][1] == True:
        print('There is milk in the room.')
    command = user_input()
    valid_command = False
    while valid_command == False:
        if command == 'south':
            valid_command = True
            pantry()
        elif command == 'east':
            valid_command = True
            courtyard()
        else:
            print('Invalid Command')
            print('You are still in the Pasture.')
            command = user_input()

def kitchen():
    print('Kitchen')
    print('room inventory', room_inventory)
    print('player inventory', player_inventory)
    if room_inventory[6][1] == True:
        print('There is a oven in the room.')
    if room_inventory[7][1] == True:
        print('There is a cake in the room.')
    command = user_input()
    valid_command = False
    while valid_command == False:
        if command == 'north':
            valid_command = True
            pantry()
        elif command == 'east':
            valid_command = True
            cupboard()
        else:
            print('Invalid Command')
            print('You are still in the Kitchen.')
            command = user_input()

def bedroom():
    print('Bedroom')
    print('room inventory', room_inventory)
    print('player inventory', player_inventory)
    if room_inventory[4][1] == True:
        print('There is a key in the room.')
    command = user_input()
    valid_command = False
    while valid_command == False:
        if command == 'north':
            valid_command = True
            chicken_coop()
        elif command == 'west':
            valid_command = True
            cupboard()
        else:
            print('Invalid Command')
            print('You are still in the Bedroom.')
            command = user_input()

def pantry():
    print('Pantry')
    print('room inventory', room_inventory)
    print('player inventory', player_inventory)
    if room_inventory[3][1] == True:
        print('There is flour in the room.')
    command = user_input()
    valid_command = False
    while valid_command == False:
        if command == 'north':
            valid_command = True
            pasture()
        elif command == 'south':
            valid_command = True
            kitchen()
        elif command == 'east':
            valid_command = True
            kings_dining_room()
        else:
            print('Invalid Command')
            print('You are still in the Pantry.')
            command = user_input()

def cupboard():
    print('Cupboard')
    print('room inventory', room_inventory)
    print('player inventory', player_inventory)
    if room_inventory[5][1] == True:
        print('There is sugar in the room.')
    command = user_input()
    valid_command = False
    while valid_command == False:
        if command == 'west':
            valid_command = True
            kitchen()
        elif command == 'north':
            valid_command = True
            kings_dining_room()
        elif command == 'east':
            valid_command = True
            bedroom()
        else:
            print('Invalid Command')
            print('You are still in the Cupboard.')
            command = user_input()

def chicken_coop():
    print('Chicken Coop')
    print('room inventory', room_inventory)
    print('player inventory', player_inventory)
    if room_inventory[2][1] == True:
        print('There are eggs in the room.')
    command = user_input()
    valid_command = False
    while valid_command == False:
        if command == 'south':
            valid_command = True
            bedroom()
        elif command == 'west':
            valid_command = True
            kings_dining_room()
        elif command == 'north':
            valid_command = True
            start_room()
        else:
            print('Invalid Command')
            print('You are still in the Chicken Coop.')
            command = user_input()

def kings_dining_room():
    print('Kings Dining Room')
    print('You lost your head!')

start_room()
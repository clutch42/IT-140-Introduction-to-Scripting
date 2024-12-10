rooms = {
        'start room': {'west': 'courtyard', 'south': 'chicken coop', 'item': '', 'locked': False},
        'courtyard': {'east': 'start room', 'south': 'kings dining room', 'west': 'pasture', 'item': 'key for cupboard', 'locked': False},
        'pasture': {'east': 'courtyard', 'south': 'pantry', 'item': 'milk', 'locked': False},
        'chicken coop': {'north': 'start room', 'west': 'kings dining room', 'south': 'bedroom', 'item': 'eggs', 'locked': False},
        'kings dining room': {},
        'pantry': {'north': 'pasture', 'east': 'kings dining room', 'south': 'kitchen', 'item': 'flour', 'locked': True},
        'bedroom': {'north': 'chicken coop', 'west': 'cupboard', 'item': 'key for pantry', 'locked': False},
        'cupboard': {'north': 'kings dining room', 'east': 'bedroom', 'west': 'kitchen', 'item': 'sugar', 'locked': True},
        'kitchen': {'north': 'pantry', 'east': 'cupboard', 'item': 'cake', 'locked': False},
        'exit': 'exit'
    }
"""
inventory = {
    'courtyard': ['key for cupboard', True],
    'pasture': ['milk', True],
    'chicken coop': ['eggs', True],
    'pantry': ['flour', True],
    'bedroom': ['key for pantry', True],
    'cupboard': ['sugar', True],
    'kitchen': ['cake', True],
    'start room': ['', False]
}
locked_rooms = {
    'chicken coop': False,
    'start room': False,
    'courtyard': False,
    'pasture': False,
    'kings dining room': False,
    'bedroom': False,
    'kitchen': False,
    'pantry': True,
    'cupboard': True
}
"""
#function to move between room
def move_between_rooms(current_room, direction):
    #if user types exit set room to exit to leave game
    if direction == 'exit':
        new_current_room = 'exit'
        return new_current_room
    #
    if rooms[current_room][direction] in locked_rooms and locked_rooms[rooms[current_room][direction]]:
        if locked_rooms['pantry'] and 'key for pantry' in player_inventory:
            locked_rooms['pantry'] = False
        if locked_rooms['cupboard'] and 'key for cupboard' in player_inventory:
            locked_rooms['cupboard'] = False
    if (locked_rooms[rooms[current_room][direction]] == True) and (rooms[current_room][direction] in locked_rooms.keys()):
        print('Locked room. You need a key to enter.')
        new_current_room = current_room
        return new_current_room
    #if the direction is valid to move rooms then set room to new room
    elif (direction in rooms[current_room]) and (direction == 'east' or direction == 'west' or direction == 'north' or direction == 'south'):
        new_current_room = rooms[current_room][direction]
    # if the direction is not valid stay in the same room
    else:
        new_current_room = current_room
        print('invalid command')
    #return the room to the program
    return new_current_room

def get_item(current_room, command, player_inventory):
    if current_room == 'kitchen' and (('milk' not in player_inventory) or ('eggs' not in player_inventory) or ('flour' not in player_inventory) or ('sugar' not in player_inventory)):
        print('You need milk, eggs, flour, and milk in order to bake the cake. Come back when you have all of the ingredients')
        return player_inventory
    if current_room in inventory and command == inventory[current_room][0] and command not in player_inventory:
        inventory[current_room][1] = False
        player_inventory.append(command)
    return player_inventory

#function to get user input and return it in a uniform manner
def user_input():
    #set initial value for command as nothing
    user_command = ''
    #while nothing has been input the loop will repeat
    #while user_command == '':
        #input from user
    user_command = input('Enter a command:')
        #strips any extra space of the beginning and end of string
    user_command = user_command.strip()
        #if nothing was input let user know invalid
        #if user_command == '':
         #   print('invalid command')
    #changes entire string to lowercase to prevent errors
    user_command = user_command.lower()
    user_command = user_command.replace('get ', '')
    #returns stripped down lowercase version of what user typed
    return user_command

#set an initial room
room = 'start room'
player_inventory = []
'''while the room is set to a room in the dictionary it will loop (once exit is typed 
exit is assigned to the room and since it's not in the dictionary it will exit)
'''
while room != 'kings dining room' and room != 'exit':
    # print current location and command options
    print('You are in the', room)
    if player_inventory != []:
        print('Player inventory: ', end='')
        for item in player_inventory:
            if player_inventory.index(item) < len(player_inventory)-1:
                print(item, end=', ')
            else:
                print(item)
    else:
        print('You have no items')
    if room in inventory:
        if inventory[room][1]:
            print('There is', inventory[room][0], 'in the room')
            print('Type get \'item\' to pick up the item')
    print('To move rooms type North, South, East, or West.')
    print('Type \'exit\' to exit')
    command = user_input()
    if command == 'exit':
        room = 'exit'
    if command in rooms[room]:
        room = move_between_rooms(room, command)
    elif command in inventory[room]:
        player_inventory = get_item(room, command, player_inventory)
    else:
        print('Invalid command')
if room == 'kings dining room' and 'cake' in player_inventory:
    print('Congragulations! You win! You made the king happy with a tasty cake and have kept your head!')
elif room == 'kings dining room' and 'cake' not in player_inventory:
    print('Oh no you don\'t have the cake! And now you don\'t have a head either! You lose.')
print('Exiting game')
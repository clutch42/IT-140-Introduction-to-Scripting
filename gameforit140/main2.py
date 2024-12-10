rooms = {
        'start room': {'west': 'courtyard', 'south': 'chicken coop'},
        'courtyard': {'east': 'start room', 'south': 'kings dining room', 'west': 'pasture'},
        'pasture': {'east': 'courtyard', 'south': 'pantry'},
        'chicken coop': {'north': 'start room', 'west': 'kings dining room', 'south': 'bedroom'},
        'kings dining room': {},
        'pantry': {'north': 'pasture', 'east': 'kings dining room', 'south': 'kitchen'},
        'bedroom': {'north': 'chicken coop', 'west': 'cupboard'},
        'cupboard': {'north': 'kings dining room', 'east': 'bedroom', 'west': 'kitchen'},
        'kitchen': {'north': 'pantry', 'east': 'cupboard'}
    }
inventory = {
    'courtyard': {'key for cupboard': True},
    'pasture': {'milk': True},
    'chicken coop': {'eggs': True},
    'pantry': {'flour': True},
    'bedroom': ['key for pantry', True],
    'cupboard': {'sugar': True},
    'kitchen': [['oven', True], ['get cake', True]],
    'player': []
}

def move_between_rooms(current_room, direction):
    #if the direction is valid to move rooms then set room to new room
    if direction in rooms[current_room]:
        new_current_room = rooms[current_room][direction]
    #if the direction is 'exit' change room to exit
    elif direction == 'exit':
        new_current_room = 'exit'
    # if the direction is not valid stay in the same room
    else:
        new_current_room = current_room
        print('invalid command')
    #return the room to the program
    return new_current_room

def get_item(current_room, command):
    print('1',current_room in inventory)
    print('2',command)
    print('3',inventory[current_room][0])
    print('4',command == inventory[current_room][0])
    if current_room in inventory and command == inventory[current_room][0]:
        inventory[current_room][1] = False
        inventory['player'] += [command]
        print('You picked up', command)
    else:
        return
    print('Your inventory: ', inventory['player'])
    return

#function to get user input and return it in a uniform manner
def user_input(current_room):
    #set initial value for command as nothing
    user_command = ''
    #while nothing has been input the loop will repeat
    while user_command == '':
        #input from user
        user_command = input('Enter a command:')
        #strips any extra space of the beginning and end of string
        user_command = user_command.strip()
        #if nothing was input let user know invalid
        if user_command == '':
            print('invalid command')
    #changes entire string to lowercase to prevent errors
    user_command = user_command.lower()
    #returns stripped down lowercase version of what user typed
    return user_command

#set an initial room
room = 'bedroom'
'''while the room is set to a room in the dictionary it will loop (once exit is typed 
exit is assigned to the room and since it's not in the dictionary it will exit)
'''
while room != 'kings dining room' and room != 'exit':
    # print current location and command options
    print('You are in the', room)
    if room in inventory:
        for index in range(len(inventory[room])):
            if index % 2 == 0 and inventory[room][index+1] == True:
                print('There is', inventory[room][index], 'in the room')
                print('Type get \'item\' to pick up the item')
    print('To move rooms type North, South, East, or West.')
    print('Type \'exit\' to exit')
    command = user_input(room)
    print(command)
    print(command.replace('get ', ''))
    print(inventory[room][0])
    if command.replace('get ', '') == inventory[room][0]:
        command = command.replace('get ', '')
        get_item(room, command)
    if command in rooms[room].values():
        room = move_between_rooms(room, command)

#Brian Engel

#dictionary for rooms, items, and whether room is locked or not
rooms = {
        'start room': {'west': 'courtyard', 'south': 'chicken coop', 'item':{'': False}, 'locked': False},
        'courtyard': {'east': 'start room', 'south': 'kings dining room', 'west': 'pasture',
                      'item': {'get key for cupboard': True}, 'locked': False},
        'pasture': {'east': 'courtyard', 'south': 'pantry', 'item': {'get milk': True}, 'locked': False},
        'chicken coop': {'north': 'start room', 'west': 'kings dining room', 'south': 'bedroom', 'item': {'get eggs': True},
                         'locked': False},
        'kings dining room': {'locked': False},
        'pantry': {'north': 'pasture', 'east': 'kings dining room', 'south': 'kitchen', 'item': {'get flour':True},
                   'locked': True},
        'bedroom': {'north': 'chicken coop', 'west': 'cupboard', 'item': {'get key for pantry': True}, 'locked': False},
        'cupboard': {'north': 'kings dining room', 'east': 'bedroom', 'west': 'kitchen', 'item': {'get sugar': True},
                     'locked': True},
        'kitchen': {'north': 'pantry', 'east': 'cupboard', 'item': {'get cake': True}, 'locked': False},
        'exit': 'exit'
}
#function to move between room
def move_between_rooms(current_room, direction):
    #if user types exit set room to exit to leave game
    if direction == 'exit':
        new_current_room = 'exit'
        return new_current_room
    #if the pantry or cupboard are locked and if the key is in inventory unlock them
    if rooms[rooms[current_room][direction]]['locked']:
        if rooms['pantry']['locked'] and 'get key for pantry' in player_inventory:
            rooms['pantry']['locked'] = False
        if rooms['cupboard']['locked'] and 'get key for cupboard' in player_inventory:
            rooms['cupboard']['locked'] = False
    #if the new room is locked keep current room
    if rooms[rooms[current_room][direction]]['locked']:
        print('Locked room. You need a key to enter.')
        new_current_room = current_room
        return new_current_room
    #if the direction is valid to move rooms then set room to new room
    elif (direction in rooms[current_room]) and (direction == 'east' or direction == 'west' or direction == 'north' or direction == 'south'):
        new_current_room = rooms[current_room][direction]
    #if the direction is not valid stay in the same room
    else:
        new_current_room = current_room
        print('invalid command')
    #return the room to the program
    return new_current_room

#function to get items
def get_item(current_room, command, player_inventory):
    #special condition for the kitchen. Need to have certain items to pick up the cake
    if current_room == 'kitchen' and (('get milk' not in player_inventory) or ('get eggs' not in player_inventory) or ('get flour' not in player_inventory) or ('get sugar' not in player_inventory)):
        print('You need milk, eggs, flour, and sugar in order to bake the cake. Come back when you have all of the ingredients')
        return player_inventory
    #if the input is a item and not in the player inventory it adds it to the player inventory and removes it from room
    for key in rooms[current_room]['item'].keys():
        if command == key and command not in player_inventory and key != '':
            rooms[current_room]['item'][key] = False
            player_inventory.append(command)
    return player_inventory

#function to get user input and return it in a uniform manner
def user_input():
    #set initial value for command as nothing
    user_command = ''
    user_command = input('Enter a command:')
    #strips any extra space of the beginning and end of string
    user_command = user_command.strip()
    #changes entire string to lowercase to prevent errors
    user_command = user_command.lower()
    #returns stripped down lowercase version of what user typed
    return user_command

#set an initial room
room = 'start room'
#set initial inventory
player_inventory = []
#set up game story line
print('The evil hungry king is going to behead you unless you bring him a cake. Navigate around the castle and collect')
print('all the ingredients but make sure not to enter the kings dining room without the cake!')
#loop until the player makes it to the kings dining room or types exit
while room != 'kings dining room' and room != 'exit':
    print('You are in the', room)
    #prints player inventory
    if player_inventory != []:
        print('Player inventory: ', end='')
        for item in player_inventory:
            if player_inventory.index(item) < len(player_inventory)-1:
                print(item.replace('get ', ''), end=', ')
            else:
                print(item.replace('get ', ''))
    else:
        print('You have no items')
    #if the item is not in player inventory prints the item in the room
    for key in rooms[room]['item'].keys():
        if key not in player_inventory and key != '':
            print('There is', key.replace('get ', ''), 'in the room')
            print('Type get \'item\' to pick up the item')
    #directions for input
    print('To move rooms type North, South, East, or West.')
    print('Type \'exit\' to exit')
    #get input from user_input function
    command = user_input()
    #if user input is exit leave game
    if command == 'exit':
        room = 'exit'
    #if user input is a direction call move_between_rooms function
    if command in rooms[room]:
        room = move_between_rooms(room, command)
    #else if input is get 'item' call get_item function
    elif command in rooms[room]['item']:
        player_inventory = get_item(room, command, player_inventory)
    #else invalid command and loop through again
    else:
        print('Invalid command')
#if player is in the kings dining room and has the cake they win
if room == 'kings dining room' and 'get cake' in player_inventory:
    print('You are in the ', room)
    print('Congragulations! You win! You made the king happy with a tasty cake and have kept your head!')
#if player is in the kings dining room and doesn't have the cake they lose
elif room == 'kings dining room' and 'get cake' not in player_inventory:
    print('You are in the ', room)
    print('Oh no you don\'t have the cake! And now you don\'t have a head either! You lose.')
print('Exiting game')
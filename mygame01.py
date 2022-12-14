#!/usr/bin/python3
"""Javier Duran
    MiniProject 2 Game"""

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands/added more instruction
    print('''
    RPG Game
    ========
    Winning the Game: Get to the Garden with a key and a potion to win! Avoid the monsters!

    Commands:
      go [direction] i.e. north, south, west, east
      get [item] i.e. pick up item in room
      press [option]
    ''')

def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)
    print(f'You have moved {moveCount} times')
    # print what the player is carrying
    print('Inventory:', inventory)
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
      print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")
    if "door" in rooms[currentRoom]:
        print("There is a door to the North, do you want to go in?")
    if "teleport" in rooms[currentRoom]:
        print("There is a button in this room, do you want to press it? Command: press button")

# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Family Room',
                  'east' : 'Dining Room',
                  'item' : 'key'
                },
            # New room added with an item
            'Family Room' : {
                'north' : 'Hall',
                'south' : 'Kitchen',
                'item' : "sword",
                "teleport" : "button"
            },
            'Kitchen' : {
                  'north' : 'Family Room',
                  'item' : 'monster'
                },
            'Dining Room' : {
                'west' : 'Hall',
                'south' : 'Garden',
                'item' : 'potion',
                "door" : "Door",
                "north" : "Trap"
                },
            'Garden' : {
                'north' : 'Dining Room'
                },
            # Trap room where player cannot escape
            "Trap" : {}
         }

# start the player in the Hall
currentRoom = 'Hall'

# variable initiated that will count how many times the player has moved
moveCount = 0

showInstructions()

# breaking this while loop means the game is over
while True:
    showStatus()

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':  
        move = input('>')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]          
    move = move.lower().split(" ", 1)

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
            # adds a count of the amount of times the player has moved
            moveCount += 1
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory.append(move[1])
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['item']
        # if there's no item in the room or the item doesn't match
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    # if they type "press" first they will be teleported to the Garden
    if move[0] == "press": 
        if "teleport" in rooms[currentRoom] and move[1] in rooms[currentRoom]["teleport"]:
            moveCount += 1
            print("You have been teleported to the Garden")
            currentRoom = "Garden"

    ## If a player enters a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you.... GAME OVER!')
        break

    ## Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory and 'sword' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break
    else:
        print('You must collect all the items in order to win')
    
    # Trap door
    if currentRoom == "Trap":
        print("You cannot escape the room.... GAME OVER!")
        break


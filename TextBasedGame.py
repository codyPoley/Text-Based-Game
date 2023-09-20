# Cody Poley

# Method status tells the player their status
def show_status(current_room, inventory):
    print('-----------------------------------------')
    # Lets the player know what room they are in
    print('You are in the', current_room)
    # Show player there inventory
    print('Inventory:', inventory)


# Method main is the main loop of the game
def main():
    # The dictionary links a room to other rooms.
    rooms = {
        'Entry Hall': {'North': 'Living Room', 'East': 'Library'},
        'Library': {'West': 'Entry Hall', 'Item': 'Sibling'},
        'Living Room': {'North': 'Garage', 'South': 'Entry Hall', 'East': "Parent's Bedroom", 'West': 'Kitchen',
                        'Item': 'Key'},
        "Parent's Bedroom": {'West': 'Living Room', 'North': 'Safe Room', 'Item': 'Gun'},
        'Kitchen': {'East': 'Living Room', 'Item': 'Silver Bullets'},
        'Safe Room': {'South': "Parent's Room"},
        'Garage': {'South': 'Living Room', 'East': 'Greenhouse', 'Item': 'Chains'},
        'Greenhouse': {'West': 'Garage', 'Item': 'Wolfbane'}
    }

    # Start player in Entry Hall
    current_room = 'Entry Hall'
    # Players Inventory
    inventory = []
    # Instructions for Player
    print('Werewolf Season')
    print('Collect all 6 items to win the game, or be eaten by your sibling.')
    print('Move commands: go North, go South, go East, go West')
    print("Add to Inventory: get 'item name'")

    while current_room != 'Safe Room':
        show_status(current_room, inventory)
        # tell the player if there is a item in the room
        if rooms.get(current_room).get('Item') is not None and rooms.get(current_room).get('Item') not in inventory:
            print('You see a', rooms.get(current_room).get('Item'))
        # Get the move from the player
        choice = input('Enter your move: ')
        # if the player enters the Safe Room it breaks
        if current_room == 'Safe Room':
            break
        # if choice is go North or go South or go East or go West
        elif choice == 'go North' or choice == 'go South' or choice == 'go East' or choice == 'go West':
            # split choice
            temp_choice = choice.split(' ')
            # choice equals temp_choice second element in the list
            choice = temp_choice[1]
            # If the player enters a direction other then the right one
            if rooms.get(current_room).get(choice) is None:
                print("You can't go that way!")
            else:
                # Changes the current room to the new room
                current_room = rooms.get(current_room).get(choice)
        # if choice is get item
        elif choice == 'get Sibling' or choice == 'get Key' or choice == 'get Gun' or choice == 'get Silver Bullets' or \
                choice == 'get Chains' or choice == 'get Wolfbane':
            # if choice equals get Silver Bullets
            if choice == 'get Silver Bullets':
                # choice equals Silver Bullets
                choice = 'Silver Bullets'
            else:
                # Split choice
                temp_choice = choice.split(' ')
                # choice equals temp_choice second element in the list
                choice = temp_choice[1]
            # if rooms item is none
            if rooms.get(current_room).get('Item') is None:
                print("This room don't have a item.")
            # if rooms item equals choice
            elif rooms.get(current_room).get('Item') == choice:
                # if choice is not in inventory
                if choice not in inventory:
                    inventory.append(choice)
                # if choice is in inventory tell the player
                else:
                    print('You have already picked up this item.')
            # Catch item if wrongly entered
            else:
                print('Invalid Item!')
        else:
            # If user enters anything other then go North, go South, go East, go West, get item, or Exit prints Invalid
            # move!
            print('Invalid move!')
        # return the inventory
    # Call for the result of the game
    result(inventory)


# Method result tells the player if they win
def result(win_condition):
    # if the size of win_condition equals 6
    if len(win_condition) == 6:
        print('Congratulations! You have made it throw the night without being eaten by your sibling!')
        print('Thank you for playing.')
        # if win_condition is less then 6
    else:
        print('GAME OVER! Your sibling has eaten you!')
        print('Thank you for playing.')


# Call main
main()



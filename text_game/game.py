from item import Item
from player import Player
from room import Room

room = {
    'outside': Room("You're outside",
                    "North of you, a bunch of scorpions\n"
                    "South of you, your front door\n"
                    "West of you, lions\n"
                    "East of you, a cartoon fairy"),
    'scorpions': Room("Scorpions", "Just step on them and continue on\n"
                      "North of you, a cave\n"
                      "The south, east and west disappeared"),
    'cave': Room("Cave", "It's just a cave"),
    'door': Room("House", """Why would you com back here?! Go north and try again!"""),
    'lions': Room("Lions", """You befriend them and they leave you alone"""),
    'fairy': Room("Fairy", "The fairy has a gun and that paralyzes you.\n"
                           "You will have to restart the game.")
}

room['outside'].n_to = room['scorpions']
room['outside'].s_to = room['door']
room['outside'].w_to = room['lions']
room['outside'].e_to = room['fairy']
room['scorpions'].n_to = room['cave']
room['door'].n_to = room['outside']

room['cave'].items.append(Item("Sword", "Sharp thing"))
room['cave'].items.append(Item("Gold", "About a dollars worth"))

name = input("Your name: ")
player = Player(name, room['outside'])

while True:
    current_room = player.current_room
    print(name, player.current_room.name)
    print(player.current_room.description)
    if current_room.items:
        print("The room contains the following items:")
        for item in current_room.items:
            print(item)
    else:
        print("This room has no items")
    user_input = input("Choose a direction to move in ('n', 's', 'e', 'w') or get or take an item: ")
    if user_input == "q":
        print("Goodbye")
        break
    split_input = user_input.split()
    print(split_input)
    if len(split_input) == 1:
        direction = f"{user_input}_to"
        if hasattr(current_room, direction):
            player.current_room = getattr(current_room, direction)
        elif user_input == "i":
            player.stuff()
        else:
            print("You can't go that way")
            continue
    elif len(split_input) == 2:
        item_name = split_input[1]
        if split_input[0].lower() == "get" or "g":
            item = current_room.get_item(item_name)
            if item:
                item.on_take()
                current_room.remove_item(item)
                player.inventory.append(item)
            else:
                print(f"There is no {item_name} in this room")
        else:
            print(f"{user_input} is not an option.")
            continue

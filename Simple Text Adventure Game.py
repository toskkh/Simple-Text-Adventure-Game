## Simple Text Adventure Game


                                                                  
                                                                  


rooms = {
    "Porch": {
        "Description": "You are standing on a porch. The door to the house is to the north. There is a path leading to the east.",
        "North": "House", 
        "East": "Garden Gate"

    },

    "Garden Gate": {
        "Description": "You are at the garden gate. You try to open it, but it is locked. You might be able to find a key somewhere... The porch is to the west.",
        "West": "Porch"
    },
    
    "House": {
        "Description": "You are inside the house. There is a hallway leading north, the kitchen to the east, and the porch to the south.",
        "North": "Hallway",
        "East": "Kitchen",
        "South": "Porch"

    },

    "Kitchen": {
        "Description": "You are in the kitchen. it smells like freshly baked cookies. The house entrance is to the west.",
        "West": "House",
    },
    
    "Hallway": {
        "Description": "You are in a dimly lit hallway. There is a door leading to the living room to the north, a bathroom to the east, stairs leading up to the second floor and the house entrance to the south.",
        "North": "Living Room",
        "East": "Bathroom",
        "Up": "Second Floor",
        "South": "House"
    },

    "Bathroom": {
        "Description": "You are in a small bathroom. There is a sink, a toilet, and a shower. The hallway is to the west.",
        "West": "Hallway"
    },

    "Living Room": {
        "Description": "You enter a cozy living room. The fire is still burning in the fireplace. There is a door that leads down to the basement in the corner of the room. The hallway is to the south.",
        "Down": "Basement",
        "South": "Hallway"
    },

    "Basement": {
        "Description": "You are in the dark, dusty basement. To the north is an ominous, dark room. To the south, is a dimly lit storage room. The boiler room is to the west, humming slowly. There are stairs leading back up to the living room.",
        "North": "Dark Room",
        "South": "Storage Room",
        "West": "Boiler Room",
        "Up": "Living Room"
    },

    "Dark Room": {
        "Description": "You are in a pitch black room. You can't see anything, but you can hear something moving around. The basement is to the south.",
        "South": "Basement"
    },

    "Storage Room": {
        "Description": "You are in a dimly lit storage room. There are boxes and shelves filled with random items. The basement is to the north.",
        "North": "Basement"
    },

    "Boiler Room": {
        "Description": "You are in the boiler room. The boiler is humming ominously. Every now and then, you hear a loud bang. The basement is to the east.",
        "East": "Basement"
    },

    "Second Floor": {
        "Description": "You are on the second floor. There is a Bedroom to the north and a Study to the south. There is a ladder leading up to the attic to the west, and the stairs that lead down to the hallway.",
        "North": "Bedroom",
        "South": "Study",
        "West": "Attic",
        "Down": "Hallway"
    },

    "Bedroom": {
        "Description": "You are in the bedroom. The bed is neatly made, and there is a walk in closet to the north. The second floor hallway is to the south.",
        "North": "Closet",
        "South": "Second Floor"
    },

    "Closet": {
        "Description": "You are in a walk in closet. There are clothes and shoeboxes everywhere. The bedroom is to the south.",
        "South": "Bedroom"
    },

    "Study": {
        "Description": "You are in the study. There is a desk with a computer on it, and a huge bookshelf filled with books. The second floor hallway is to the north.",
        "North": "Second Floor"
    },

    "Attic": {
        "Description": "You are in the attic. There are boxes, old furniture, and cobwebs everywhere. You feel like you are being watched. The second floor hallway is to the east.",
        "East": "Second Floor"
    }

}

current_room = "Porch"

print("==============================")
print("Welcome to the Adventure Game!")
print("==============================")

while True:
    print("\n--------------------------------")
    print(rooms[current_room]["Description"])
    print("--------------------------------")

    move = input("Where would you like to go? (type 'quit' to exit) ").strip().capitalize()
    if move == "Quit":
        print("Thanks for playing!! cya next time!")
        break
    if move in rooms[current_room]:
        current_room = rooms[current_room][move]
    else:
        print("\n[!] You can't go that way!. Read the description carefully and try again.")

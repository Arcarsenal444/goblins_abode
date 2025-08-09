
"""
goblins_abode
check_items.py
@author: arcarsenal444
purpose: this file executes each time the player-character enters
a room to determine whether the pc has already acquired certain items.
"""


# imports

from tkinter import *
import time
from playsound3 import playsound


def check_items(hero_obj, room_name):

    # FLOOR 1: DOWNSTAIRS

    if room_name == "Entry Way" and "A sack to hold items" not in hero_obj.character_items:
        time.sleep(3)
        print("From the floor you collect a cloth sack to hold items.\n")
        hero_obj.add_items("A sack to hold items")
        time.sleep(3)


    elif room_name == "Main Hall" and "rusty dagger" not in hero_obj.character_items:
        print("A rusty dagger lies on the ground beneath the table.")
        time.sleep(2)
        print("Do you take the rusty dagger?")

        # Creating a new window and configurations
        window = Tk()
        window.title("Goblins' Abode")
        window.minsize(width=300, height=75)

        label = Label(text="Rusty Dagger")
        label.pack()

        def radio_used():
            print("\nYou take the rusty dagger...\n")
            # playsound(r"C:\Users\Joshb\Desktop\goblins_abode\dagger_whoosh.wav")
            playsound(r"sfx\dagger_whoosh.wav")

        def radio_used_2():
            print("\nYou leave the rusty thing lying in place.")

        # Variable to hold on to which radio button value is checked.
        radio_state = IntVar()
        radiobutton1 = Radiobutton(text="Yes", value=1, variable=radio_state, command=radio_used)
        radiobutton2 = Radiobutton(text="No", value=2, variable=radio_state, command=radio_used_2)
        radiobutton1.pack()
        radiobutton2.pack()
        window.mainloop()

        if radio_state.get() == 1:
            hero_obj.character_items.append("rusty dagger")
        elif radio_state.get() == 2:
            pass


    elif room_name == "Try Lock" and "skeleton key" in hero_obj.character_items:
        print("The box is empty. You've already collected the skeleton key.")


    elif room_name == "Try Lock" and "rusty dagger" not in hero_obj.character_items:
        print("You fiddle with the lock, but alas it cannot be opened by fingers alone. Perhaps if you tried \n"
              "an implement of some sort. Looks like this could be pried open with a narrow blade. It's no use \n"
              "otherwise.")


    elif room_name == "Try Lock" and "rusty dagger" in hero_obj.character_items:
        # Creating a new window and configurations
        window = Tk()
        window.title("Goblins' Abode")
        window.minsize(width=300, height=200)

        # Labels
        label = Label(text="Open the small box")
        label.pack()

        # Buttons
        def open_box():
            print("Inside the box you find a sterling silver key with a death's head on the grip.\n")
            time.sleep(3)
            hero_obj.add_items("skeleton key")
            print("You have collected the skeleton key.\n")

        # calls action() when pressed
        button = Button(text="Try dagger", command=open_box)
        button.pack()
        window.mainloop()


    elif room_name == "Parlor" and "Bit of brie: eaten" not in hero_obj.character_items:
        print("In the corner, you spy a wedge of brie. Do you dare eat the brie?")
        # Creating a new window and configurations
        window = Tk()
        window.title("Goblins' Abode")
        window.minsize(width=300, height=75)

        label = Label(text="Bit of brie")
        label.pack()

        def radio_used():
            print("\nThe choice has been made...\n")

        # Variable to hold on to which radio button value is checked.
        radio_state = IntVar()
        radiobutton1 = Radiobutton(text="Yes", value=1, variable=radio_state, command=radio_used)
        radiobutton2 = Radiobutton(text="No", value=2, variable=radio_state, command=radio_used)
        radiobutton1.pack()
        radiobutton2.pack()
        window.mainloop()

        if radio_state.get() == 1:
            print("If it smells like feet it's good to eat. Down the hatch.")
            hero_obj.character_items.append("Bit of brie: eaten")
            if hero_obj.character_hp < hero_obj.character_total_hp - 5:
                hero_obj.character_hp += 5
            else:
                hero_obj.character_hp = hero_obj.character_total_hp
            time.sleep(2)
            print("You've just increased your hp.")
        elif radio_state.get() == 2:
            pass


    # FLOOR 1: UPSTAIRS

    elif room_name == "Open Chest" and "stone coin" not in hero_obj.character_items:
        print("\nIn the middle rests a stone coin, the size of your palm. "
              "Also on the coin is an engraving of a sparrow")
        print("\n\nDo you take the coin?")
        window = Tk()
        window.title("Goblins' Abode")
        window.minsize(width=300, height=75)

        label = Label(text="Take the Coin?")
        label.pack()

        def radio_used():
            print("\nThe choice has been made...\n")

        # Variable to hold on to which radio button value is checked.
        radio_state = IntVar()
        radiobutton1 = Radiobutton(text="Yes", value=1, variable=radio_state, command=radio_used)
        radiobutton2 = Radiobutton(text="No", value=2, variable=radio_state, command=radio_used)
        radiobutton1.pack()
        radiobutton2.pack()
        window.mainloop()

        if radio_state.get() == 1:
            print("You have taken the stone coin.")
            hero_obj.character_items.append("stone coin")
        elif radio_state.get() == 2:
            pass


    elif room_name == "Open Chest" and "stone coin" in hero_obj.character_items:
        print("You've already taken the stone coin.")


    elif room_name == "Closet" and "skeleton key" not in hero_obj.character_items:
        print("Perhaps if you had some sort of key.\n")
        time.sleep(2)
        print("What do you choose to do?")
        return False


    elif room_name == "Closet" and "skeleton key" in hero_obj.character_items:
        # Creating a new window and configurations
        window = Tk()
        window.title("Goblins' Abode")
        window.minsize(width=300, height=200)

        # Labels
        label = Label(text="Open the door in the closet")
        label.pack()

        # Buttons
        def open_door():
            print("\nUsing the skeleton key, the lock mechanism clinks and the door swings wide open.\n")
            time.sleep(2)
            print("A short, narrow hallway leads deeper into darkness.\n")

        # calls action() when pressed
        button = Button(text="Use skeleton key", command=open_door)
        button.pack()
        window.mainloop()
        return True

# NEW: WRITING THIS TO END LEVEL 1

    elif room_name == "Spiral Stair" and "stone coin" in hero_obj.character_items:
        # Creating a new window and configurations
        window = Tk()
        window.title("Goblins' Abode")
        window.minsize(width=300, height=200)

        # Labels
        label = Label(text="Open the door to the spiral stair")
        label.pack()

        # Buttons
        def open_door():
            print("\nThe stone coin thunks into the slot, the lock mechanism clinks, and the door grinds wide open.\n")
            time.sleep(2)
            print("In a dim shaft of light you see that you stand at the base of a spiral staircase made of wrought \n"
                  "iron.")

        # calls action() when pressed
        button = Button(text="Use stone coin", command=open_door)
        button.pack()
        window.mainloop()
        return True

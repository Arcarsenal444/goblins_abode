
"""
goblins_abode
decision_tree.py
@author: arcarsenal444
purpose: this file collects the choices the player-character confronts
in each room, manufactures the tkinter window to make those choices
actionable, and returns the selected choice, thereby advancing the pc
through the game.
"""


# imports

from tkinter import *


# decision function

def decision(decision_dict):

    if len(decision_dict) == 5:

        # setting variables

        room_name = decision_dict["room_name"]

        decision_list_from_dict = list(decision_dict.items())

        option_1 = decision_list_from_dict[0][0]
        option_2 = decision_list_from_dict[1][0]
        option_3 = decision_list_from_dict[2][0]
        option_4 = decision_list_from_dict[3][0]
        decision_1 = decision_list_from_dict[0][1]
        decision_2 = decision_list_from_dict[1][1]
        decision_3 = decision_list_from_dict[2][1]
        decision_4 = decision_list_from_dict[3][1]

        # creating tkinter mechanism

        window = Tk()
        window.title("Goblins' Abode")
        window.minsize(width=300, height=75)

        label = Label(text=room_name)  # This is a dict, so I'm calling the entry; IT HAS TO MATCH CASE!
        label.pack()

        def radio_used():
            print("\nThe choice has been made...\n")

        radio_state = IntVar()
        radiobutton1 = Radiobutton(text=option_1, value=1, variable=radio_state, command=radio_used)
        radiobutton2 = Radiobutton(text=option_2, value=2, variable=radio_state, command=radio_used)
        radiobutton3 = Radiobutton(text=option_3, value=3, variable=radio_state, command=radio_used)
        radiobutton4 = Radiobutton(text=option_4, value=4, variable=radio_state, command=radio_used)
        radiobutton1.pack()
        radiobutton2.pack()
        radiobutton3.pack()
        radiobutton4.pack()
        window.mainloop()

        if radio_state.get() == 1:
            return decision_1
        elif radio_state.get() == 2:
            return decision_2
        elif radio_state.get() == 3:
            return decision_3
        elif radio_state.get() == 4:
            return decision_4

    elif len(decision_dict) == 4:

        # setting variables

        room_name = decision_dict["room_name"]

        decision_list_from_dict = list(decision_dict.items())

        option_1 = decision_list_from_dict[0][0]
        option_2 = decision_list_from_dict[1][0]
        option_3 = decision_list_from_dict[2][0]
        decision_1 = decision_list_from_dict[0][1]
        decision_2 = decision_list_from_dict[1][1]
        decision_3 = decision_list_from_dict[2][1]

        # creating tkinter mechanism

        window = Tk()
        window.title("Goblins' Abode")
        window.minsize(width=300, height=75)

        label = Label(text=room_name)  # This is a dict, so I'm calling the entry; IT HAS TO MATCH CASE!
        label.pack()

        def radio_used():
            print("\nThe choice has been made...\n")

        radio_state = IntVar()
        radiobutton1 = Radiobutton(text=option_1, value=1, variable=radio_state, command=radio_used)
        radiobutton2 = Radiobutton(text=option_2, value=2, variable=radio_state, command=radio_used)
        radiobutton3 = Radiobutton(text=option_3, value=3, variable=radio_state, command=radio_used)
        radiobutton1.pack()
        radiobutton2.pack()
        radiobutton3.pack()
        window.mainloop()

        if radio_state.get() == 1:
            return decision_1
        elif radio_state.get() == 2:
            return decision_2
        elif radio_state.get() == 3:
            return decision_3


# --------------------------------------------------------------------------------
# THIS VERSION WORKS IF THE NEW VERSION WITH DIFFERENCES FOR DICTS OF LEN 4 OR 5 DOESN'T.


# # imports
#
# from tkinter import *
#
#
# # decision function
#
# def decision(decision_dict):
#
#     # setting variables
#
#     room_name = decision_dict["room_name"]
#
#     decision_list_from_dict = list(decision_dict.items())
#
#     option_1 = decision_list_from_dict[0][0]
#     option_2 = decision_list_from_dict[1][0]
#     option_3 = decision_list_from_dict[2][0]
#     option_4 = decision_list_from_dict[3][0]
#     decision_1 = decision_list_from_dict[0][1]
#     decision_2 = decision_list_from_dict[1][1]
#     decision_3 = decision_list_from_dict[2][1]
#     decision_4 = decision_list_from_dict[3][1]
#
#     # creating tkinter mechanism
#
#     window = Tk()
#     window.title("Goblins' Abode")
#     window.minsize(width=300, height=75)
#
#     label = Label(text=room_name)  # This is a dict, so I'm calling the entry; IT HAS TO MATCH CASE!
#     label.pack()
#
#     def radio_used():
#         print("\nThe choice has been made...\n")
#
#     radio_state = IntVar()
#     radiobutton1 = Radiobutton(text=option_1, value=1, variable=radio_state, command=radio_used)
#     radiobutton2 = Radiobutton(text=option_2, value=2, variable=radio_state, command=radio_used)
#     radiobutton3 = Radiobutton(text=option_3, value=3, variable=radio_state, command=radio_used)
#     radiobutton4 = Radiobutton(text=option_4, value=4, variable=radio_state, command=radio_used)
#     radiobutton1.pack()
#     radiobutton2.pack()
#     radiobutton3.pack()
#     radiobutton4.pack()
#     window.mainloop()
#
#     if radio_state.get() == 1:
#         return decision_1
#     elif radio_state.get() == 2:
#         return decision_2
#     elif radio_state.get() == 3:
#         return decision_3
#     elif radio_state.get() == 4:
#         return decision_4


# --------------------------------------------------------------------------------

# NOTE: This is the former version, the un-altered version, before I started
# to mess with the keys and values in the radio buttons and radio_state.gets

# def decision(decision_list_from_dict):
#
#     room_name = decision_list_from_dict["room_name"]
#
#     # Do I have to convert it to another dictionary? And use that dict below?
#     # then make each value its own entry, like option_1 = decision_list_from_dict[0][1]
#     # option_2 = decision_list_from_dict[1][1], and so forth...
#
#     window = Tk()
#     window.title("Goblins' Abode")
#     window.minsize(width=300, height=75)
#
#     label = Label(text=room_name)  # This is a dict, so I'm calling the entry; IT HAS TO MATCH CASE!
#     label.pack()
#
#     def radio_used():
#         print("\nThe choice has been made...\n")
#
#     # TODO: this is where to start next. we have to fix the .NAME[] placeholders to reflect the dictionary info.
#     # Variable to hold on to which radio button value is checked.
#     radio_state = IntVar()
#     radiobutton1 = Radiobutton(text=decision_list_from_dict.KEY[0], value=1, variable=radio_state, command=radio_used)
#     radiobutton2 = Radiobutton(text=decision_list_from_dict.KEY[1], value=2, variable=radio_state, command=radio_used)
#     radiobutton3 = Radiobutton(text=decision_list_from_dict.KEY[2], value=3, variable=radio_state, command=radio_used)
#     radiobutton4 = Radiobutton(text=decision_list_from_dict.KEY[3], value=4, variable=radio_state, command=radio_used)
#     radiobutton1.pack()
#     radiobutton2.pack()
#     radiobutton3.pack()
#     radiobutton4.pack()
#     window.mainloop()
#
#     if radio_state.get() == 1:
#         return decision_list_from_dict.VALUE[0]
#     elif radio_state.get() == 2:
#         return decision_list_from_dict.VALUE[1]
#     elif radio_state.get() == 3:
#         return decision_list_from_dict.VALUE[2]
#     elif radio_state.get() == 4:
#         return decision_list_from_dict.VALUE[3]
#         # might have to do something like decision(decision_list_from_dict, hero) here.
#         # or you might have to return the command and do it in the main.
#         # Or maybe display items() if that's a function, and it formats it nicely...
#         # Probably that's better. call hero.display_items

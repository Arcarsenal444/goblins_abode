
"""
goblins_abode
character.py
@author: arcarsenal444
purpose: the character class that creates the
player-character object once per game.
"""


# imports

import time
import persistence
import os

# Character class

class Character:
    def __init__(self, character_hp, character_total_hp, character_gold, character_name,
                 character_level, character_xp, character_attack_strength, floor_level):
        self.character_hp = character_hp
        self.character_total_hp = character_total_hp
        self.character_gold = character_gold
        self.character_name = character_name
        self.character_level = character_level
        self.character_xp = character_xp
        self.character_attack_strength = character_attack_strength
        self.floor_level = floor_level
        self.character_items = ["small sword"]

    def to_json(self):
        j={
            'character_hp':self.character_hp,
            'character_total_hp':self.character_total_hp,
            'character_gold':self.character_gold,
            'character_name':self.character_name,
            'character_level':self.character_level,
            'character_xp':self.character_xp,
            'character_attack_strength':self.character_attack_strength,
            'floor_level':self.floor_level,
            'character_items':self.character_items
        }
        return j

    def from_json(self, j = {}):
        self.character_hp = j['character_hp']
        self.character_total_hp = j['character_total_hp']
        self.character_gold = j['character_gold']
        self.character_name = j['character_name']
        self.character_level = j['character_level']
        self.character_xp = j['character_xp']
        self.character_attack_strength = j['character_attack_strength']
        self.floor_level = j['floor_level']
        self.character_items = j['character_items']

    def save(self, o_dir=''):
        j = self.to_json()
        ofname = f'{o_dir}/{self.character_name}.json'
        persistence.save_json(ofname, j)
        print(f'- status: saved {self.character_name} to {ofname}')

    def load(self, o_dir=''):
        ofname = f'{o_dir}/{self.character_name}.json'
        j = persistence.load_json(ofname)
        self.from_json( j )
        print(f'- status: loaded  {self.character_name} from  {ofname}')

    def already_saved(self, o_dir=''):
        ofname = f'{o_dir}/{self.character_name}.json'
        if os.path.exists(ofname):
            return True
        return False

    def load_if_saved(self, o_dir=''):
        ofname = f'{o_dir}/{self.character_name}.json'
        if self.already_saved(o_dir):
            self.load(o_dir)

    def character_perish(self):
        print("The goblin's thrust slices into your heart. You stagger and gasp your last breath.")
        time.sleep(3)
        print(f"The goblin vanquishes {self.character_name}. You perish where you lie.")

    def add_items(self, new_item):
        self.character_items.append(new_item)

    def show_items(self):
        print("--------------------------------------")
        print("Current hp: " + str(self.character_hp))
        print("Current total hp: " + str(self.character_total_hp))
        print("Current xp: " + str(self.character_xp))
        print("Current gold: " + str(self.character_gold) + " ivars")
        print("Current level: " + str(self.character_level))
        print("Held items: " + str(self.character_items))
        print("Currently on Floor " + str(self.floor_level))
        print("--------------------------------------")
        print("\n")
        time.sleep(3)


"""
The below code was originally in this file 
but has since been moved to a battle file; 
it was originally at one indent level
"""

# def character_attack(self):
#     if self.character_hp <= 0:
#         self.perish()
#     else:
#         print("You ready yourself to attack...")
#
#         # Creating a new window and configurations
#         window = Tk()
#         window.title("Goblins' Abode")
#         window.minsize(width=500, height=500)
#
#         # Labels
#         label = Label(text="Attack")
#         label.pack()
#
#         # Buttons
#         def attack_roll():
#             attack_roll = random.randint(1, 20)
#             print("Your trusty sword thrusts at your foe...")
#             time.sleep(3)
#             print("Roll: " + str(attack_roll))
#
#         # calls action() when pressed
#         button = Button(text="Roll", command=attack_roll)
#         button.pack()
#
#         if attack_roll >= 12:
#             print("You slice into the goblin's crusty skin, eliciting a howl of pain and anger!")
#             damage()
#         else:
#             print("Your feint and parry fail...")
#
#
# def damage():
#     # Creating a new window and configurations
#     window = Tk()
#     window.title("Goblins' Abode")
#     window.minsize(width=500, height=500)
#
#     # Labels
#     label = Label(text="Damage")
#     label.pack()
#
#     # Buttons
#     def damage_roll():
#         damage_roll = random.randint(1, 7)
#         print(f"The blow delivers {damage_roll} points of damage.")
#         return damage_roll
#
#     # calls action() when pressed
#     button = Button(text="Roll", command=damage)
#     button.pack()

"""
And this was originally a function, but now it's
taken care of in the level_up.py file
"""

# def increase_hp(self, new_hp):
# self.character_hp += new_hp




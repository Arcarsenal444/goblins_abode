
"""
goblins_abode
level_up.py
@author: arcarsenal444
purpose: this file is executed each time after the player-character
wins a battle to see if the pc has amassed enough experience points
to increase the level. (as the pc's level increases so too does its
strength and abilities.)
"""


def level_increase(hero_obj):

    if hero_obj.character_level == 1 and hero_obj.character_xp > 100:
        hero_obj.character_level = 2
        hero_obj.character_total_hp = hero_obj.character_total_hp + 5
        hero_obj.character_hp = hero_obj.character_total_hp
        hero_obj.character_attack_strength += 1
        print("++++++++++++++++++++++++++++++++++++")
        print(f"Your character level increased to {hero_obj.character_level}.")
        print(f"Your hp level increased to {hero_obj.character_total_hp}")
        print("Your attack strength also increased.")
        print("++++++++++++++++++++++++++++++++++++")
        print("\n\n")

    elif hero_obj.character_level == 2 and hero_obj.character_xp > 200:
        hero_obj.character_level = 3
        hero_obj.character_total_hp = hero_obj.character_total_hp + 5
        hero_obj.character_hp = hero_obj.character_total_hp
        hero_obj.character_attack_strength += 1
        print("++++++++++++++++++++++++++++++++++++")
        print(f"Your character level increased to {hero_obj.character_level}.")
        print(f"Your hp level increased to {hero_obj.character_total_hp}")
        print("Your attack strength also increased.")
        print("++++++++++++++++++++++++++++++++++++")
        print("\n\n")

    elif hero_obj.character_level == 3 and hero_obj.character_xp > 300:
        hero_obj.character_level = 4
        hero_obj.character_total_hp = hero_obj.character_total_hp + 5
        hero_obj.character_hp = hero_obj.character_total_hp
        hero_obj.character_attack_strength += 1
        print("++++++++++++++++++++++++++++++++++++")
        print(f"Your character level increased to {hero_obj.character_level}.")
        print(f"Your hp level increased to {hero_obj.character_total_hp}")
        print("Your attack strength also increased.")
        print("++++++++++++++++++++++++++++++++++++")
        print("\n\n")

    elif hero_obj.character_level == 4 and hero_obj.character_xp > 400:
        hero_obj.character_level = 5
        hero_obj.character_total_hp = hero_obj.character_total_hp + 5
        hero_obj.character_hp = hero_obj.character_total_hp
        hero_obj.character_attack_strength += 1
        print("++++++++++++++++++++++++++++++++++++")
        print(f"Your character level increased to {hero_obj.character_level}.")
        print(f"Your hp level increased to {hero_obj.character_total_hp}")
        print("Your attack strength also increased.")
        print("++++++++++++++++++++++++++++++++++++")
        print("\n\n")

    elif hero_obj.character_level == 5 and hero_obj.character_xp > 500:
        hero_obj.character_level = 6
        hero_obj.character_total_hp = hero_obj.character_total_hp + 5
        hero_obj.character_hp = hero_obj.character_total_hp
        hero_obj.character_attack_strength += 1
        print("++++++++++++++++++++++++++++++++++++")
        print(f"Your character level increased to {hero_obj.character_level}.")
        print(f"Your hp level increased to {hero_obj.character_total_hp}")
        print("Your attack strength also increased.")
        print("++++++++++++++++++++++++++++++++++++")
        print("\n\n")

    elif hero_obj.character_level == 6 and hero_obj.character_xp > 600:
        hero_obj.character_level = 7
        hero_obj.character_total_hp = hero_obj.character_total_hp + 5
        hero_obj.character_hp = hero_obj.character_total_hp
        hero_obj.character_attack_strength += 1
        print("++++++++++++++++++++++++++++++++++++")
        print(f"Your character level increased to {hero_obj.character_level}.")
        print(f"Your hp level increased to {hero_obj.character_total_hp}")
        print("Your attack strength also increased.")
        print("++++++++++++++++++++++++++++++++++++")
        print("\n\n")

    elif hero_obj.character_level == 7 and hero_obj.character_xp > 700:
        hero_obj.character_level = 8
        hero_obj.character_total_hp = hero_obj.character_total_hp + 5
        hero_obj.character_hp = hero_obj.character_total_hp
        hero_obj.character_attack_strength += 1
        print("++++++++++++++++++++++++++++++++++++")
        print(f"Your character level increased to {hero_obj.character_level}.")
        print(f"Your hp level increased to {hero_obj.character_total_hp}")
        print("Your attack strength also increased.")
        print("++++++++++++++++++++++++++++++++++++")
        print("\n\n")

    elif hero_obj.character_level == 8 and hero_obj.character_xp > 800:
        hero_obj.character_level = 9
        hero_obj.character_total_hp = hero_obj.character_total_hp + 5
        hero_obj.character_hp = hero_obj.character_total_hp
        hero_obj.character_attack_strength += 1
        print("++++++++++++++++++++++++++++++++++++")
        print(f"Your character level increased to {hero_obj.character_level}.")
        print(f"Your hp level increased to {hero_obj.character_total_hp}")
        print("Your attack strength also increased.")
        print("++++++++++++++++++++++++++++++++++++")
        print("\n\n")

    elif hero_obj.character_level == 9 and hero_obj.character_xp > 900:
        hero_obj.character_level = 10
        hero_obj.character_total_hp = hero_obj.character_total_hp + 5
        hero_obj.character_hp = hero_obj.character_total_hp
        hero_obj.character_attack_strength += 1
        print("++++++++++++++++++++++++++++++++++++")
        print(f"Your character level increased to {hero_obj.character_level}.")
        print(f"Your hp level increased to {hero_obj.character_total_hp}")
        print("Your attack strength also increased.")
        print("++++++++++++++++++++++++++++++++++++")
        print("\n\n")

    else:
        pass

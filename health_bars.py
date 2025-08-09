
"""
goblins_abode
health_bars.py
@author: arcarsenal444
purpose: this file displays the player-character and goblin
health bars that appear during battles.
"""


import emoji

"""
just thinking out loud, but if the hero's hp will go up 
over time, i'll have to run a percentage check and assign 
each bar to a particular percentage of hp vs. total hp, 
which means I'll have to add a character_total_hp to the 
hero class, probably to the goblins as well...

I may have to make this into a function that takes in the 
hero's hp and total hp (and same for goblins) and then 
prints the bars back in the battle_file.py file when called."""


# display health bars function

def display_health_bars(hero_obj, goblin_obj):

    hero_health_12 = f"{hero_obj.character_name}: 🟥🟥🟥🟥🟨🟨🟨🟨🟩🟩🟩🟩"
    hero_health_11 = f"{hero_obj.character_name}: 🟥🟥🟥🟨🟨🟨🟨🟩🟩🟩⬜"
    hero_health_10 = f"{hero_obj.character_name}: 🟥🟥🟥🟥🟨🟨🟨🟨🟩🟩⬜⬜"
    hero_health_9 = f"{hero_obj.character_name}: 🟥🟥🟥🟥🟨🟨🟨🟨🟩⬜⬜⬜"
    hero_health_8 = f"{hero_obj.character_name}: 🟥🟥🟥🟥🟨🟨🟨🟨⬜⬜⬜⬜"
    hero_health_7 = f"{hero_obj.character_name}: 🟥🟥🟥🟥🟨🟨🟨⬜⬜⬜⬜⬜"
    hero_health_6 = f"{hero_obj.character_name}: 🟥🟥🟥🟥🟨🟨⬜⬜⬜⬜⬜⬜"
    hero_health_5 = f"{hero_obj.character_name}: 🟥🟥🟥🟥🟨⬜⬜⬜⬜⬜⬜⬜"
    hero_health_4 = f"{hero_obj.character_name}: 🟥🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜"
    hero_health_3 = f"{hero_obj.character_name}: 🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜⬜"
    hero_health_2 = f"{hero_obj.character_name}: 🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜"
    hero_health_1 = f"{hero_obj.character_name}: 🟥⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜"
    hero_death = f"{hero_obj.character_name}: 💀💀💀💀💀💀💀💀💀💀💀💀"

    # Goblin's health bars

    goblin_health_12 = "Goblin: 🟥🟥🟥🟥🟨🟨🟨🟨🟩🟩🟩🟩\n"
    goblin_health_11 = "Goblin: 🟥🟥🟥🟥🟨🟨🟨🟨🟩🟩🟩⬜\n"
    goblin_health_10 = "Goblin: 🟥🟥🟥🟥🟨🟨🟨🟨🟩🟩⬜⬜\n"
    goblin_health_9 = "Goblin: 🟥🟥🟥🟥🟨🟨🟨🟨🟩⬜⬜⬜\n"
    goblin_health_8 = "Goblin: 🟥🟥🟥🟥🟨🟨🟨🟨⬜⬜⬜⬜\n"
    goblin_health_7 = "Goblin: 🟥🟥🟥🟥🟨🟨🟨⬜⬜⬜⬜⬜\n"
    goblin_health_6 = "Goblin: 🟥🟥🟥🟥🟨🟨⬜⬜⬜⬜⬜⬜\n"
    goblin_health_5 = "Goblin: 🟥🟥🟥🟥🟨⬜⬜⬜⬜⬜⬜⬜\n"
    goblin_health_4 = "Goblin: 🟥🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜\n"
    goblin_health_3 = "Goblin: 🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜⬜\n"
    goblin_health_2 = "Goblin: 🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜\n"
    goblin_health_1 = "Goblin: 🟥⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜\n"
    goblin_death = "Goblin: 💀💀💀💀💀💀💀💀💀💀💀💀\n"

    hero_percentage = int(hero_obj.character_hp / hero_obj.character_total_hp * 100)
    goblin_percentage = int(goblin_obj.goblin_hp / goblin_obj.goblin_total_hp * 100)

    if hero_percentage >= 92:
        print(emoji.emojize(hero_health_12))
    elif 92 > hero_percentage >= 84:
        print(emoji.emojize(hero_health_11))
    elif 84 > hero_percentage >= 76:
        print(hero_health_10)
    elif 76 > hero_percentage >= 68:
        print(hero_health_9)
    elif 68 > hero_percentage >= 60:
        print(hero_health_8)
    elif 60 > hero_percentage >= 52:
        print(hero_health_7)
    elif 52 > hero_percentage >= 44:
        print(hero_health_6)
    elif 44 > hero_percentage >= 36:
        print(hero_health_5)
    elif 36 > hero_percentage >= 28:
        print(hero_health_4)
    elif 28 > hero_percentage >= 20:
        print(hero_health_3)
    elif 20 > hero_percentage >= 12:
        print(hero_health_2)
    elif 12 > hero_percentage >= 1:
        print(hero_health_1)
    elif hero_percentage < 1:
        print(hero_death)

    if goblin_percentage >= 90:
        print(goblin_health_12)
    elif 92 > goblin_percentage >= 84:
        print(goblin_health_11)
    elif 84 > goblin_percentage >= 76:
        print(goblin_health_10)
    elif 76 > goblin_percentage >= 68:
        print(goblin_health_9)
    elif 68 > goblin_percentage >= 60:
        print(goblin_health_8)
    elif 60 > goblin_percentage >= 52:
        print(goblin_health_7)
    elif 52 > goblin_percentage >= 44:
        print(goblin_health_6)
    elif 44 > goblin_percentage >= 36:
        print(goblin_health_5)
    elif 36 > goblin_percentage >= 28:
        print(goblin_health_4)
    elif 28 > goblin_percentage >= 20:
        print(goblin_health_3)
    elif 20 > goblin_percentage >= 12:
        print(goblin_health_2)
    elif 12 > goblin_percentage >= 1:
        print(goblin_health_1)
    elif goblin_percentage < 1:
        print(goblin_death)

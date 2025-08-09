
"""
goblins_abode
floor_2.py
@author: arcarsenal444
purpose: this file assembles all the rooms from the second floor, each
of which contains a dictionary of choices that the player-character will
select from in order to advance.
"""


# imports

import time
from check_items import check_items

# climage is how I'm showing graphics at the moment, but it's not a good solution
# import climage

# Also trying to show graphics using PIL
# from PIL import Image

# Also trying to show graphics using os
# import os

# Also trying IPython
# from IPython.display import Image, display


# Initiate choice

def initiate_rooms(hero, room_name):  # (hero, room_name) will have to go in most of these below...
    if room_name == "Living Room":
        destination_dict = living_room()
        return destination_dict
    if room_name == "Shrine":
        destination_dict = shrine()
        return destination_dict
    if room_name == "Map Room":
        destination_dict = map_room()
        return destination_dict
    if room_name == "Grand Ballroom":
        destination_dict = grand_ballroom()
        return destination_dict
    if room_name == "Smoking Room":
        destination_dict = smoking_room()
        return destination_dict
    if room_name == "":
        destination_dict = eastern_alcove()
        return destination_dict
    if room_name == "":
        destination_dict = examine_bust()
        return destination_dict
    if room_name == "":
        destination_dict = open_bust()
        return destination_dict
    if room_name == "":
        destination_dict = try_lock()
        return destination_dict
    if room_name == "":
        destination_dict = western_alcove()
        return destination_dict
    if room_name == "":
        destination_dict = inspect_sphere()
        return destination_dict
    if room_name == "":
        destination_dict = parlor()
        return destination_dict
    if room_name == "":
        destination_dict = grand_staircase()
        return destination_dict
    if room_name == "":
        destination_dict = second_floor_landing()
        return destination_dict
    if room_name == "":
        destination_dict = master_bedroom()
        return destination_dict
    if room_name == "":
        destination_dict = open_chest()
        return destination_dict
    if room_name == "":
        destination_dict = north_hall()
        return destination_dict
    if room_name == "":
        destination_dict = garret_room()
        return destination_dict
    if room_name == "":
        destination_dict = closet()
        return destination_dict
    if room_name == "":
        destination_dict = spiral_stair()
        return destination_dict


# room descriptions

def living_room():

    # This is for loading the image when the time comes
    # output = climage.convert("4x4.jpg") # This is a placeholder
    # print(output)
    # time.sleep(2)

    # And here's my image attempt with PIL/Pillow (this shows it in a pop-up window though)
    # img = Image.open("4x4.jpg")
    # img.show()

    # And here's my attempt with os (also opens in pop-up window)
    # os.system("4x4.jpg")

    # And here's my attempt with IPython.display (this does not work)
    # display(Image(filename="4x4.jpg"))

    print("Living Room\n\n"
          "A vast and shadowy living room confronts you. Above the grand, carved fireplace, a mantel is strewn with \n"
          "objets d'art, including a small cluster of three silvery metal cubes. A vaulted ceiling blossoms overhead \n"
          "where shadows cluster and the gloom pervades. The centerpiece of the room is the bearskin rug, surrounded \n"
          "by three ornate sophas. Haunting portraits painted in smoky oils loom from the walls, and an antique grand\n"
          "father clock stands mute in the corner, its pendulum motionless. The remains of a dog's carcass lie in a \n"
          "pool of blackened blood, its organs harvested for unknown purposes. Three-toed footprints in dried blood \n"
          "zig-zag across the fraying persian carpets. \n"
          "Embellished doorways stand open to the north, east, and south.\n\n")
    time.sleep(2)
    # check_items(hero, room_name)
    time.sleep(2)
    print("\nDo you proceed north, east, or south?")
    destination_dict = {"North": "Shrine", "East": "Grand Ballroom", "South": "Map Room", "Items": "Items",
                        "room_name": "Living Room"}
    return destination_dict


# ---------------------------------------------------------------------------------------------------


def shrine():

    print("A Shrine\n\n"
          "This room, lit only by a wealth of weltering candles, feels shrouded in an almost impenetrable gloom, \n"
          "which lurks in corners and canvasses the ceiling. Against the red-painted north wall, a small wooden \n"
          "altar stands waist high. On its pentagonal surfaces lie the remains of a burnt offering (likely some \n"
          "small woodland animal from the nearby forest) and a sacrificial dagger with a serpentine blade. Painted \n"
          "on the wall above the altar are the words 'CALL UNTO HIM' and the image of a six-pointed star is rendered \n"
          "in a careful hand. The ornamentation is wreathed in a garland of black silks, lace, twigs, and leaves. \n"
          "Three small metal pyramids stand in a perfect horizontal line in front of the altar.\n\n")
    time.sleep(2)
    # HERE'S WHERE WE RUN A CHECK FOR SOMETHING IN HIS INVENTORY OR SOME MARKER, THAT TRIGGERS THIS ABOUT THE CODE:
    # the words 'LBR HWL NXS' but save those for the Lodge. Here let's use
    # check_code(hero)
    # check_items(hero, room_name)
    time.sleep(2)
    print("Do you go south, X, or Y?")
    destination_dict = {"South": "Living Room", "a": "", "b": "", "Items": "Items",
                        "room_name": "Shrine"}
    return destination_dict


# ---------------------------------------------------------------------------------------------------


def map_room():

    print("The Map Room\n\n"
          "You enter a room in the shape of a perfect cube, the every inch of which (excepting the floor) is covered \n"
          "in maps of great antiquity. In the center of the floor stands a massive wooden globe, several feet in dia-\n"
          "meter, ensconced in an ornately carved pedestal of dark wood. Studying the wall maps for a moment, you see \n"
          "that both the parchment and handwriting appear ancient, and the descriptions of the continents are not as \n"
          "you know them to be."
          # Prob here ask if you want to inspect the globe y/n.
          "Approaching the globe, you see it too envisages a far more primordial time when the continents arrayed them-\n"
          "selves in altogether unnatural formations, beneath night skies upon which the stars tell a different tale \n"
          "than they tell today."
          # Here discover the compartment. open y/n.
          "\n\n")
    time.sleep(2)
    # check_items(hero, room_name)
    # playsound(r"C:\Users\Joshb\Desktop\goblins_abode\dagger_whoosh.wav")
    time.sleep(2)
    print("Do you go north, south, east, or west?")
    destination_dict = {"North": "Living Room", "East": "Obelisk Room", "b": "", "Items": "Items",
                        "room_name": "Map Room"}
    return destination_dict


# ---------------------------------------------------------------------------------------------------


def grand_ballroom():

    print("A Grand Ballroom\n\n"
          "You come into a grand ballroom that miraculously has been left untouched by the destructive forces at \n"
          "work so assiduously in most other parts of this lair. A circular stage, elevated to a height of about \n"
          "three feet, stands in the center of the oblong room. The parquet floor is immaculately polished, and \n"
          "folding chairs stand in arrow-straight rows along each wall. Streamers dangle from the ceiling, their \n"
          "speckled texture glistening softly in the room's gentle darkness. A refreshments table sits covered in \n"
          "a strata of dust, and the punch bowl is scummed over, and may be heard to hiss occasionally. On the \n"
          "wall a plaque has been buffed to a glowing sheen.")
    time.sleep(2)

# if something, then trigger the question about looking at the plaque.
# plaque reads: THE MEMORIALS OF YESTERDAY SHALL BE THE MEMORIALS OF TOMORROW; WE ARE IN THE SPIRAL, ALWAYS.

    print("Doorways open to the north, east, and west.")


# ---------------------------------------------------------------------------------------------------


def smoking_room():

    print("Smoking Room\n\n"
          "A dark crimson-colored smoking room presents itself, its most consequential ornamentation, the boutique \n"
          "ceramic smoking urns, are overturned, though that is, thankfully, the extent of the upset to the room. \n"
          "Its lushly papered walls remain in tact and unscathed, as does the upholstery of a small armada of \n"
          "leather wing back chairs and foot rests. An oil painting on the east wall depicts and astrologer of old, \n"
          "replete with flowing robe and beard, staring balefully into a philosopher's stone. \n"
          "Etched in the frame are the words WE OPEN DOORS")
    time.sleep(2)

# something to do in this room?
    print("The only doorway leads back to the south.")


# ---------------------------------------------------------------------------------------------------


def obelisk_room():

    print("Obelisk Room\n\n"
          "This near-empty room feels as though it has not beheld a presence in months if not years, so vacant and \n"
          "absent of affectation are the wood-panelled walls and hard wood floor, so chilled and stale is the atmos- \n"
          "phere. The ledge of the window on the south wall is sheathed in undisturbed dust. The space contains, \n"
          "however, an alien presence in the form of a looming, menacing, obsidian obelisk monolith, faceted cruelly \n"
          "and jaggedly. Its splintered crown brushes the high ceiling. In hammered tin beside the statue this plaque \n"
          "is bolted to the floor: BERALANESIS, BALDACHIENSIS, PAUMACHIA, APOLOGIA SEDES.")
    time.sleep(2)

    # if something is in inventory, we won't trigger this riddle game.
    # CHANCE TO GET INCREASED MAX HP POTION WITH A RIDDLE THAT OPENS THE BOX.
    # A small wooden box rests on the otherwise unremarkable floor. A folded note rests on the top of the box.
    # unfolded, it reads: health yada


# ---------------------------------------------------------------------------------------------------


def room_of_mirrors():

    print("Room of Mirrors\n\n"
          "Instantly you feel yourself to be floating amidst an endlessly branching spiders-web of corridors that \n"
          "capture your obedient likeness out into infinity. The floor and ceiling likewise are mirrored, casting \n"
          "you mercilessly into a branching dimension and making you even less certain of your footing. Too much \n"
          "time spent here could have you questioning reality. An anomaly catches your eye. A crack in one pane low \n"
          "on the wall reveals a hint of writing on the surface beneath. You could pick out the glass to look more \n"
          "closely, though handling broken mirrors comes with risks. Do you investigate?")


"""
For these room where the codes (---/---/---) are written, it will trigger to ask you if you want 
to investigate if you don't have the code already. Once you have a given code, it gets stored somewhere
so that you aren't asked again. (kind of like the brie)
"""

"""
If you opt to remove the glass, you will roll the dice to see if you cut your hand or remove the glass 
safely. If not, you lose HP. This gamble, the possibility of losing HP to learn the codes, happens for 
each of the three codes.
"""


# ---------------------------------------------------------------------------------------------------


def laboratory():

    print("The Laboratory\n\n"
          "The laboratory inexplicably thrums with life, its archaic but well-preserved instruments and paraphernalia \n"
          "all ready for immediate indulgence. Certain gas-powered contraptions sputter and whir, supplying electricity \n"
          "to power the lab's manifold data processing machines. A riot of miniscule, translucent, ill-formed tenta- \n"
          "cles writhe out of a set of scummed-over test tubes. Spread around the room are beakers, flasques, burners, \n"
          "and reams of litmus paper."
          "Doorways open to the south, east, and west."


# ---------------------------------------------------------------------------------------------------


def druid_chamber():

    print("The Druid Chamber\n\n"
          "You step down into a stone-walled chamber. Open windows to the east and south carry away the smoke borne of \n"
          "torch light. Several tapestries, woven by master artisans, depict ancient foreign deities with cities for \n"
          "heads and forests of black obelisks. The center of the room is dominated by a low, star-shaped dais, on which \n"
          "stands a blood-red altar. Various wands and staves, gauntlets and talismans lie scattered akimbo across its \n"
          "vast gnarled surface. On one corner there rests a small cylinder of jade. There's something strange about the \n"
          "cylinder, you feel, that perhaps something is contained within."


# ---------------------------------------------------------------------------------------------------


def torture_room():

    print("Torture Room\n\n"
          "Too many unspeakable acts were herein committed. Of this place we shall speak no more out of respect.")


# ---------------------------------------------------------------------------------------------------


def lodge():

    print("The Lodge\n\n"
          "You recognize the room to be in the style of a 1960s midwestern Elks Lodge, with its low stage at one end, \n"
          "a kitchen besides, and linoleum-tiled meeting room, which hosts a dozen folding tables and chairs."
          "SMTH SMTH SMTH."
          "You spy a loose panel in the wall just above the mounting of an antlered Elks Lodge turban. Reaching between \n"
          "those sharp antlers could be risky. Will you >>>>>>???")

"""
Same function plays out here for taking a chance to read the code ---/---/---
"""

# Finish with "Doors open to the south and west."


# ---------------------------------------------------------------------------------------------------


def room_echoing_darkness():

    print("The Room of Echoing Darkness\n\n"
          "The walls of this room are fuzzy and indistinct, so dim it is, that they are barely visible. A light source \n"
          "is variously hinted at but never pinned down. Strange and ghastly noises echo across the space and are heard \n"
          "to diminish in the distance. In the approximate center of this swirling room stands a pillar, on top of which \n"
          "sits a scale, its arms disbalanced by XXXXXXXXX")



"""
Here's how this works: the jade statue gets placed in some scales and the balance is struck.
Ding! A door opens, beyond which a spiral staircase...
"""







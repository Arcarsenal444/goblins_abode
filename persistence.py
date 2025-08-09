
"""
goblins abode
persistence.py
@author: arcarsenal444
purpose:
    - provide the functions to save/load as json files/dictionaries
    - can be used to save arbitrary data structures
    - in particular things like:
        - a given character's "bag" of info - i.e., health, level, etc.
        - a given level, other game params, etc.
    - will need main code to create, manage, and check these dictionaries for logic
    - then just call these to save/load
"""

import json
import os


def make_json_output_dir( o_dir='' ):
    os.makedirs(o_dir, exist_ok = True)

# assume: ofname = f'{output_dir/output_filename.json'
def save_json(ofname='', j={}):
    try:
        of = open(ofname, 'w', encoding='utf-8')
        of.write(json.dumps(j, indent=True))
        of.close()
    except Exception as e:
        print( f'- error: problem saving json file: {ofname}')
        exit()

def load_json(ifname=''):
    j={}
    try:
        j = json.loads(open(ifname, encoding='utf-8').read())
    except Exception as e:
        print(f'- error: problem loading json file: {ifname}')
        exit()
    return j

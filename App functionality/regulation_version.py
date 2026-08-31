import Save_state_manipulation as ssm
import Character_extraction as ce
import button_functionality as bf
import Gui_functionality as guif
from pathlib import Path
import os
import json
import unicodedata


game_modes = ["normal", "abc"]
save_folder = Path(os.getenv("LOCALAPPDATA")) / "DBD Challenge Tracking App" / "Saves"

def save_file_normalization(character_name, save_file_name):
    character_list = ssm.check_character_state(character_name,save_file_name)

    path = f'{save_folder}/{character_name}/{save_file_name}.json'
    mode = next(iter(character_list))

    format_incorrect(character_list, path, mode)
    missing_characters(character_list,character_name,path, mode)

    # Re-read file to get sorted data that was saved by missing_characters()
    character_list = ssm.check_character_state(character_name,save_file_name)
    return character_list



def format_incorrect(character_list, path, mode):
    if mode not in game_modes:
        data = {}
        data["normal"] = character_list

        with open(path,'w') as file:
            json.dump(data, file, indent=4)


def missing_characters(character_list, character_name, path, mode):

    dir_keys = list(character_list[mode])
    print
    if mode == "normal":
        if character_name == "Killers":
            checking_keys = ce.killer_list()[:-1]
        elif character_name == "Survivors":
            checking_keys = ce.survivor_list()[:-1]
    elif mode == "abc":
        if character_name == "Killers":
            checking_keys = ce.killer_perks()
        elif character_name == "Survivors":
            checking_keys = ce.survivor_perks()
    if set(dir_keys) == set(checking_keys):
        return
    else:
        missing_chars = set(checking_keys) - set(dir_keys)

        if next(iter(character_list)) == "normal":
            data = character_list
            for char in missing_chars:
                data["normal"][char] = 0

            with open(path, 'w') as file:
                json.dump(data, file, indent= 4)

        elif next(iter(character_list)) == "abc":
            data = {}
            data1 = character_list["abc"]
            for char in missing_chars:
                data1[char] = 0

            def remove_accents(text):
                return ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')
            
            data1 = dict(sorted(data1.items(), key=lambda x: remove_accents(x[0])))
            data["abc"] = data1

            with open(path, 'w') as file:
                json.dump(data, file, indent=4)
    
    return







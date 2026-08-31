import Character_extraction as ce
import Image_extraction as ie
import json
import os
import customtkinter
import button_functionality as bf
import Gui_functionality as guif
from pathlib import Path

save_folder = Path(os.getenv("LOCALAPPDATA")) / "DBD Challenge Tracking App" / "Saves"

def close_pop_up(master):
    tw = getattr(master, "toplevel_window", None)
    if tw and tw.winfo_exists():
        try:
            tw.destroy()
        finally:
            master.toplevel_window = None

def open_top_level(master, character, name):

    information = name

    if master.toplevel_window is None or not master.toplevel_window.winfo_exists():
        master.toplevel_window = save_file_window(master, character, information)
        master.toplevel_window.focus()
    else:
        master.toplevel_window.focus()

    

class save_file_window(customtkinter.CTkToplevel):
    def __init__(self, master, character, name):
        super().__init__()

        self.transient(master)
        self.lift()
        self.geometry("400x150")
        
        self.main_app = master  # Store reference to main app

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=2)

        self.path = f"{save_folder}/{character}"
        self.save_name = name

        self.radio_var = customtkinter.IntVar(value = 0)

        self.radbutton1 = customtkinter.CTkRadioButton(self, text="Normal Mode", variable = self.radio_var, value=1)
        self.radbutton2 = customtkinter.CTkRadioButton(self, text="ABC Mode", variable = self.radio_var, value=2)

        self.radbutton1.grid(row = 1, column= 0, padx= 10, pady=10)
        self.radbutton2.grid(row = 2, column= 0, padx= 10, pady=10)        


        self.closebutton = customtkinter.CTkButton(self, text= "Close", command= lambda: close_pop_up(master))
        self.createbutton = customtkinter.CTkButton(self, text= "Create", command = lambda: createsave(self, self.main_app, character_type=character, save_name=name))

        self.closebutton.grid(row = 3, column = 0, padx= 10, pady= 10)
        self.createbutton.grid(row = 3, column = 1, padx= 10, pady= 10)

        
def createsave(master, masterapp, character_type, save_name):
    save_mode = master.radio_var.get()
    if save_mode == 1:
        save_file_creation(master, character_type, save_name, 1)
        close_pop_up(masterapp)
        bf.switch_window(masterapp,guif.MakeAndChooseSaves(masterapp, char_type=character_type))
    elif save_mode == 2:
        save_file_creation(master, character_type, save_name, 2)
        close_pop_up(masterapp)
        bf.switch_window(masterapp,guif.MakeAndChooseSaves(masterapp, char_type=character_type))

def open_save_menu(master, character_type:str, save_name:str):
    open_top_level(master, character_type, save_name)

def save_file_creation(master, character_type:str, save_name:str, state):
    final_dict = {}

    if state == 1:
        character_dict = {}
        if character_type == "Killers":
            character_list = ce.killer_list()
        elif character_type == "Survivors":
            character_list = ce.survivor_list()


        for i in character_list[:-1]:
            character_dict[i] = 0

        final_dict["normal"] = character_dict

    elif state == 2:
        perk_dict = {}

        if character_type == "Killers":
            perk_list = ce.killer_perks()
        elif character_type == "Survivors":
            perk_list = ce.survivor_perks()

        for i in perk_list:
            perk_dict[i] = 0

        final_dict["abc"] = perk_dict

    with open(f"{save_folder}/{character_type}/{save_name}.json", "w", encoding="utf-8") as f:
        json.dump(final_dict,f,indent=4)        

def modify_character_state(char_type:str,save_name:str,character:str,new_state:int):

    path = f'{save_folder}/{char_type}/{save_name}.json'

    with open(path,'r') as file:
        data = json.load(file)
    mode = next(iter(data))
    data[mode][character] = new_state

    with open(path,'w') as file:
        json.dump(data, file, indent=4)


def check_character_state(char_type:str,save_name:str):
    path = f'{save_folder}/{char_type}/{save_name}.json'
    print(Path(path).resolve())
    with open(path,'r') as file:
        data = json.load(file)
    return data


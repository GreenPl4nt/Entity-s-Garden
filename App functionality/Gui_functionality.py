import customtkinter
import Character_extraction as ce
import Image_extraction as ie
import Save_state_manipulation as ssm
import button_functionality as bf
import Update_functionality as uf
import regulation_version as rv
from pathlib import Path
import pywinstyles
import os

appdata_path = os.getenv("LOCALAPPDATA")

TRANSPARENT_BACKGROUND = "#000001"

#Complete sintetized functionality of frame for Killers and Survivors

class FunctionalGrid(customtkinter.CTkScrollableFrame):
    def __init__(self, master, character_name:str,save_file_name:str):
        super().__init__(master, fg_color=TRANSPARENT_BACKGROUND)

        pywinstyles.set_opacity(self, color=TRANSPARENT_BACKGROUND)

        bg_lable = customtkinter.CTkLabel(self._parent_canvas, text="", image=ie.bg_images()[f"{character_name}_background"])
        bg_lable.grid(row=0, column=0, sticky="nsew")
        bg_lable.lower()
  

        self.save_name = save_file_name
        self.font = customtkinter.CTkFont(family="Roboto", size=15, weight="bold")
        self.character_name = character_name



        self.save = rv.save_file_normalization(character_name, save_file_name)
        self.game_mode = next(iter(self.save))
        self.save_state = self.save[next(iter(self.save))]
        self.labels = []
        self.buttons_dict = {}



        self.character = list(self.save_state.keys())
        cleaned_names = [char.replace('"','').replace(':','') for char in self.character]

        self.icons = ie.other_images(self.game_mode, character_name, cleaned_names)  
        
        self.character_images = ie.extract_images(f"./Info/assets/Character assets/",character_name,cleaned_names, self.game_mode)
        
        column = 0
        row = 0

        for i in self.character:
            self.grid_columnconfigure(column, weight=1)
            cleaned_name = i.replace('"','').replace(':','')

#Button functionality for Killers

            if self.character_name == "Killers":
                char_label = customtkinter.CTkLabel(self, text=f"The {i}" if self.game_mode == "normal" else i)
                char_label.lift()

                if self.save_state[i] == 0:
                    char_button = customtkinter.CTkButton(self, 
                                                          image=self.character_images[cleaned_name], 
                                                          text="", 
                                                          fg_color="transparent",
                                                          command=lambda cn=i, on_img=self.character_images[cleaned_name], 
                                                                                  off_img=self.icons[cleaned_name] if self.game_mode == "abc" else self.icons["dead survivor"]: bf.switch_image(self,button=self.buttons_dict[cn],
                                                                                  save=save_file_name,
                                                                                  character=cn,
                                                                                  on_image=on_img,
                                                                                  off_image=off_img,
                                                                                  char_type=character_name))
                    char_button.lift()

                elif self.save_state[i] == 1:
                    char_button = customtkinter.CTkButton(self,
                                                          image=self.icons[cleaned_name] if self.game_mode == "abc" else self.icons["dead survivor"],
                                                          text="", 
                                                          fg_color="transparent",
                                                          command=lambda cn=i, on_img=self.character_images[cleaned_name], off_img=self.icons[cleaned_name] if self.game_mode == "abc" else self.icons["dead survivor"]: bf.switch_image(self,button=self.buttons_dict[cn],
                                                                                  save=save_file_name,
                                                                                  character=cn,
                                                                                  on_image=on_img,
                                                                                  off_image=off_img,
                                                                                  char_type=character_name))
            
#Button functionality for survivors

            elif self.character_name == "Survivors":
                char_label = customtkinter.CTkLabel(self, text=i, font=self.font)
                char_label.lift()

                if self.save_state[i] == 0:
                    char_button = customtkinter.CTkButton(self, 
                                                          image=self.character_images[cleaned_name], 
                                                          text="", 
                                                          fg_color="transparent",
                                                          command=lambda cn=i, on_img=self.character_images[cleaned_name], off_img=self.icons[cleaned_name] if self.game_mode == "abc" else self.icons["dead survivor"]: bf.switch_image(self,button=self.buttons_dict[cn],
                                                                                  save=save_file_name,
                                                                                  character=cn,
                                                                                  on_image=on_img,
                                                                                  off_image=off_img,
                                                                                  char_type=character_name))
                    char_button.lift()

                elif self.save_state[i] == 1:
                    char_button = customtkinter.CTkButton(self,
                                                          image=self.icons[cleaned_name] if self.game_mode == "abc" else self.icons["dead survivor"],
                                                          text="", 
                                                          fg_color="transparent",
                                                          command=lambda cn=i, on_img=self.character_images[cleaned_name], off_img=self.icons[cleaned_name] if self.game_mode == "abc" else self.icons["dead survivor"]: bf.switch_image(self,button=self.buttons_dict[cn],
                                                                                  save=save_file_name,
                                                                                  character=cn,
                                                                                  on_image=on_img,
                                                                                  off_image=off_img,
                                                                                  char_type=character_name))
      
            char_button.grid(row=row+1, column=column, padx= 10, pady= (0,10))
            char_label.grid(row=row, column=column, padx= 10, pady= (0,10))
            
            char_button.image = self.character_images[cleaned_name]
            self.buttons_dict[i] = char_button

            if column == 3:
                row += 2
                column = 0
            else:
                column += 1 
            
            self.labels.append(char_label)

#Window functionality to make and/or choose which save to use
#TODO: Make a pop up to choose which gamemode to make the save

class MakeAndChooseSaves(customtkinter.CTkFrame):
    def __init__(self, master, char_type:str):
        super().__init__(master)

        self.row = 1
        self.grid_columnconfigure(0, weight=1)
        self.save_path = Path(appdata_path) / "DBD Challenge Tracking App" / "Saves" / char_type

        dir_path = Path(self.save_path)
        files_list = [i for i in dir_path.iterdir() if i.is_file()]



        for i in files_list:

            self.grid_rowconfigure(self.row, weight=1)
            save_name = Path(f"{self.save_path}/{i}").stem
            if char_type == "Killers": 
      

                save_button = customtkinter.CTkButton(self, 
                                                    text=f"{save_name}",
                                                    command= lambda save=save_name, : bf.switch_window(master,FunctionalGrid(master, 
                                                                                                        character_name=char_type,
                                                                                                        save_file_name= save)))
            elif char_type == "Survivors" : 
                save_button = customtkinter.CTkButton(self, 
                                                    text=f"{save_name}",
                                                    command= lambda save=save_name, : bf.switch_window(master,FunctionalGrid(master, 
                                                                                                        character_name=char_type,
                                                                                                        save_file_name= save)))                
            save_button.grid(row=self.row,column=0,padx= 10, pady= (10,10),sticky="ew")
            self.row += 1


        self.controls_frame = customtkinter.CTkFrame(self)
        self.controls_frame.grid(row=0, columnspan=3, sticky="ew")
        self.controls_frame.grid_columnconfigure(0, weight=1)
        self.controls_frame.grid_columnconfigure(1, weight=0)
        self.controls_frame.grid_columnconfigure(2, weight=0)

        self.create_text = customtkinter.CTkEntry(self.controls_frame, placeholder_text="this is where you put your save file name")
        self.create_button = customtkinter.CTkButton(self.controls_frame, text="Create Save file", command= lambda: bf.create_savefile(master, self, char_type))

        self.create_text.grid(row=0, columnspan=2, padx=10, pady=10, sticky="ew")
        self.create_button.grid(row=0, column=2, padx=10, pady=10, sticky="ew")



#Main menu frame that allows for changing between the killers and survivors

class MainMenu(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")
        
        self.rowconfigure(0, weight=1)
        self.columnconfigure((0,1,2), weight=1)

        bg_lable = customtkinter.CTkLabel(self, text="", image=ie.bg_images()["main_menu_bg"])
        bg_lable.grid(row=0, column=0, columnspan=3, rowspan=2, sticky="nsew")    


        killerbutton = customtkinter.CTkButton(self, 
                                               text="", 
                                               image= ie.other_images()["killers_icon"],
                                               fg_color="black",
                                               width=0,
                                               height=0,
                                               corner_radius=0,
                                               command= lambda: bf.switch_window(master,MakeAndChooseSaves(master,char_type="Killers")))
        killerbutton.grid(row=0,column=0, padx= 10, pady= (0,10))        
        pywinstyles.set_opacity(killerbutton,color="black")

        killerbutton.lift()

        survivorbutton = customtkinter.CTkButton(self, text="", 
                                                 image= ie.other_images()["survivors_icon"],
                                                 fg_color="black",
                                                 width=0,
                                                 height=0,                                                 
                                                 command= lambda: bf.switch_window(master,MakeAndChooseSaves(master,char_type="Survivors")))
        survivorbutton.grid(row=0,column=1, padx= 10, pady= (0,10))
        pywinstyles.set_opacity(survivorbutton,color="black")        
        survivorbutton.lift()
        
        updatebutton = customtkinter.CTkButton(self, text="", 
                                               image= ie.other_images()["update_icon"],
                                               fg_color="black",
                                               width=0,
                                               height=0,                                               
                                               command= lambda: uf.check_for_updates(master, version=master.version))       
        updatebutton.grid(row=0, column=2, padx= 10, pady= (0,10))
        pywinstyles.set_opacity(updatebutton,color="black")
        updatebutton.lift()



#Main Window class 

class MainApp(customtkinter.CTk):
    def __init__(self, app_version):
        super().__init__()
        self.version = app_version
        self.title(f"DBD-Challenge-Tracking-App - {self.version}")
        self.geometry("900x500")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


        self.funcgrid = MainMenu(self) 
        self.funcgrid.grid(row= 0, column= 0, columnspan=2, padx= 0, pady= (10,0), sticky="nsew")
        madeby_label = customtkinter.CTkLabel(
            self,
            text = "Made by GreenPlant",
            font = ("Arial", 10, "bold"),
        )
        version_label = customtkinter.CTkLabel(
            self,
            text=f"Version {self.version}",
            font=("Arial", 10, "bold"),
            anchor="e",
        )
        madeby_label.grid(row=1, column=0, sticky="sw", padx= 10, pady= 10)
        version_label.grid(row=1, column=1, sticky="se", padx=10, pady=10)

        self.toplevel_window = None

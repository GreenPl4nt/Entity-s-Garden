import Save_state_manipulation as ssm
import customtkinter
import Character_extraction as ce

def switch_image(master,button,char_type,save,character,on_image,off_image):
    state = ssm.check_character_state(char_type=char_type,save_name=save)
    interm = state[next(iter(state))]
    char_state = interm[character]

    if char_state == 0:
        button.configure(text="", image=off_image)
        ssm.modify_character_state(char_type=char_type,save_name=save,character=character,new_state=1)
        return
    elif char_state == 1:
        button.configure(text="", image=on_image)
        ssm.modify_character_state(char_type=char_type,save_name=save,character=character,new_state=0)
        return
    

def switch_window(master, frame_class):
    if master.funcgrid is not None:
        try:
            master.funcgrid.destroy()
        except:
            pass
    master.funcgrid = frame_class
    master.funcgrid.grid(row= 0, column= 0, columnspan= 2, padx= 0, pady= (10,0), sticky="nsew")
    master.update_idletasks()


def create_savefile(master, frame, char_type):
    import Gui_functionality as guif
    save_name = frame.create_text.get()
    ssm.open_save_menu(master,char_type,save_name=save_name)
"""     if char_type == "Killers": 
        save_button = customtkinter.CTkButton(frame, 
                                            text=f"{save_name}",
                                            command= lambda save=save_name, : switch_window(master,guif.FunctionalGrid(master, 
                                                                                                characters=ce.killer_list(), 
                                                                                                character_name=char_type,
                                                                                                save_file_name= save)))
    elif char_type == "Survivors" : 
        save_button = customtkinter.CTkButton(frame, 
                                            text=f"{save_name}",
                                            command= lambda save=save_name, : switch_window(master,guif.FunctionalGrid(master, 
                                                                                                characters=ce.survivor_list(), 
                                                                                                character_name=char_type,
                                                                                                save_file_name= save)))   
    save_button.grid(row=frame.row,column=0,padx= 10, pady= (10,10),sticky="ew")

    frame.row += 1 """


    
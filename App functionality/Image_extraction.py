import customtkinter
from PIL import Image

#Creates an image, might make it so that the images scale with the window size

def other_images(game_mode = None, char_type = None, clist = None):
     path = f"./Info/assets/icons/"
     icons = ["dead survivor", "killers_icon" , "survivors_icon", "update_icon"]
     img_dict = {}
     for i in icons:
          image = customtkinter.CTkImage(light_image= Image.open(f"{path}/{i}.png"),
                                        size=(242,242))
          img_dict[i] = image

     if game_mode == "abc":
          for i in clist:
               other_path = f"./Info/assets/Character assets/{char_type}/Perks/Final/{i}.png"
               image = customtkinter.CTkImage(light_image=Image.open(other_path),
                                              size = (256,256))
               img_dict[i] = image
          
     return img_dict

def extract_images(path:str,character_name,clist:list, game_mode):
     img_dict = {}

     if game_mode == "normal":
          image_path = f"{path}/{character_name}/Characters"
          for i in clist:
               image = customtkinter.CTkImage(light_image= Image.open(f"{image_path}/{i}.png"),
                                                  size=(242,242))
               img_dict[i] = image
          
     elif game_mode == "abc":
          image_path = f"{path}/{character_name}/Perks/Initial"

          for i in clist:
               image = customtkinter.CTkImage(light_image=Image.open(f"{image_path}/{i}.png"),
                                                  size=(256,256) )
               img_dict[i] = image

     return img_dict


def bg_images():
     path="./Info/assets/backgrounds/"
     backgrounds = ["main_menu_bg", "Killers_background", "Survivors_background"]
     img_dict = {}

     for i in backgrounds:
          image = customtkinter.CTkImage(light_image= Image.open(f"{path}/{i}.jpg"),
                                                                size= (1920,839))
          img_dict[i] = image

     return img_dict
import customtkinter
from PIL import Image

#Creates an image, might make it so that the images scale with the window size

def other_images():
     path = f"./Info/assets/icons/"
     icons = ["dead survivor", "killers_icon" , "survivors_icon", "update_icon"]
     img_dict = {}
     for i in icons:
          image = customtkinter.CTkImage(light_image= Image.open(f"{path}/{i}.png"),
                                        size=(242,242))
          img_dict[i] = image

     return img_dict

def extract_images(path:str,clist:list):
    img_dict = {}
    for i in clist [:-1]:
         image = customtkinter.CTkImage(light_image= Image.open(f"{path}/{i}.png"),
                                        size=(242,242))
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
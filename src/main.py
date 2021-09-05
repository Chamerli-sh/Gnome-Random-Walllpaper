import os
import random
import getpass

user_name = getpass.getuser()
image_format = ["png", "jpg", "jpeg"]

# This one is used so that it can change the background cause for some reason finding the image and chousing the background use totally difrent systems
path = "/Pictures"

true_path = random.choice(os.listdir("/home/"+ user_name + path))

def change_wallpaper(new_path):
    os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri " + new_path)

def get_file_path():
    true_path = random.choice(os.listdir("/home/"+ user_name + path))
    return true_path

def valid_image_check(ver_path):
    actual_file_format = ver_path.split(".")[-1]

    if actual_file_format in image_format:
        print(ver_path)
        return True
    else:
        print(ver_path)
        return False


if valid_image_check(get_file_path()) == True:
    change_wallpaper(get_file_path())
else:
    change_wallpaper(get_file_path())

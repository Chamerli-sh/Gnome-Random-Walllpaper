import os
import random
import getpass

user_name = getpass.getuser()

# This one is used so that it can change the background cause for some reason finding the image and chousing the background use totally difrent systems
path = "/Pictures"

true_path = random.choice(os.listdir("/home/"+ user_name + path))

def change_wallpaper(path):
    os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri " + path)

def get_file_path():
    true_path = random.choice(os.listdir("/home/"+ user_name + path))
    return true_path

change_wallpaper("~/" + path + "/" + get_file_path())
print(get_file_path())
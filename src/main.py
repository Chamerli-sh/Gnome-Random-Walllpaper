import os
import random
import getpass

user_name = getpass.getuser()
path = random.choice(os.listdir("/home/"+ user_name +"/Pictures"))


def change_wallpaper(path):
    os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri " + path)

def get_file_path():
    path = random.choice(os.listdir("/home/"+ user_name +"/Pictures"))
    return path

change_wallpaper(path)
print("p" + get_file_path())
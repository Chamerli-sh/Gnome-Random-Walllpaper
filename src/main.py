import os
import random
import getpass
import time

user_name = getpass.getuser()
image_format = ["png", "jpg", "jpeg"]

# This one is used so that it can change the background cause for some reason finding the image and chousing the background use totally difrent systems
path = "/Pictures"

true_path = random.choice(os.listdir("/home/"+ user_name + path))

def change_wallpaper(new_path):
    os.system("gsettings set org.gnome.desktop.background picture-uri file:" + new_path)

def get_file_path():
    true_path = random.choice(os.listdir("/home/"+ user_name + path))
    return true_path

def valid_image_check(ver_path):
    actual_file_format = ver_path.split(".")[-1]

    if actual_file_format in image_format:
        print(true_path)
        return True
    else:
        print(ver_path)
        return False

def contdown(t):
    while t > 0:
        print(t)
        t -= 1
        time.sleep(1)
    
    if t <= 0:
        get_file_path()
        true_path = random.choice(os.listdir("/home/"+ user_name + path))
        change_wallpaper("/home/"+ user_name + path + "/" + true_path)
        print("Current wallpaper: " + true_path)
while True:
    contdown(10)
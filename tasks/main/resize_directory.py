from tasks.main import config as c
import os
from PIL import Image


def resize(name):
    files_lst = os.listdir(os.getcwd()+ "\\" +c.directory_name + "\\" + name)
    folder_name = f"resized_{name}"
    if folder_name in os.listdir(c.size_directory):
        for file in os.listdir(c.size_directory + "\\" + folder_name):
            os.remove(c.size_directory + "\\" + folder_name + "\\" + file)
        os.rmdir(c.size_directory + "\\" +folder_name)

    os.mkdir(c.size_directory+ "\\" + folder_name)

    for filename in files_lst:
        if filename[filename.find(".") + 1:] == "db":
            continue
        try:
            with Image.open(os.getcwd() + "\\" + c.directory_name + "\\" + name + "\\" + filename) as image:

                img = image.resize((c.width, c.height))
                img = img.convert("RGB")
                img.save(os.getcwd() + "\\" + c.size_directory + "\\" + folder_name + "\\" + filename)
        except IOError:
            pass

import config as c
import os
from PIL import Image


def check_size(directory):
    files_lst = os.listdir(directory)

    for filename in files_lst:
        with Image.open(os.path.join(filename, directory)) as image:
            if not image.size == (c.width, c.height):
                return False
    return True

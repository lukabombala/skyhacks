from resize_directory import resize
from print_size import check_size
import config as c
import os

lst = os.listdir("main_task_data")

# for directory in lst:
#    print(str(check_size(os.path.join("resized", directory))) + f" {directory}")
os.mkdir("resized3")
for name in lst:
    resize(name)
    print(f"resized {name}")

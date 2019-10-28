from tasks.main.resize_directory import resize
import os

lst = os.listdir("main_task_data")

# for directory in lst:
#    print(str(check_size(os.path.join("resized", directory))) + f" {directory}")
os.mkdir("resized3")
for name in lst:
    resize(name)
    print(f"resized {name}")

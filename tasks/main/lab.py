import pandas as pd
import os
import shutil

df = pd.read_csv('labels_updated.csv')

data = df[['filename', 'task2_class', 'Bathroom', 'Bedroom', 'Dining room', 'House', 'Kitchen', 'Living room']]

folder_name = "validation"
lst = os.listdir(folder_name)
os.mkdir("val")
a = dict()
for index, row in data.iterrows():
    for column in data.columns:
        if row[column] == 1 and row['task2_class'] == "validation":
            a[row['filename']] = column

counter = 0
for name in lst:
    _class = a[name[:-4]]
    if _class not in os.listdir("val"):
        os.mkdir(f"val\\{_class}")
    shutil.copy(f"validation\\{name}", f"val\\{_class}")
    counter += 1
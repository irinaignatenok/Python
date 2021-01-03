
import os
import datetime

os.scandir()

files = os.scandir()#Not recursive(Search inside this folder only)

for file in files:
    #print(file)
    pass
# . --> current folder
#.. --> Parent folder
files = os.walk('.')# Recursive!(He searches in all the subfolders!)

for file in files:
    # print(file)
    pass

# don't need to close with
with open("file.txt", "w") as f:
    f = open(filepath, "w")
    f.write(f"{today_date.day}/{today_date.month}/{today_date.year}")
    f.writelines(["Hello", "World"])


today_date = datetime.datetime.now()
filepath = "file.txt"
# full_path = "/irinaignat/Desktop"

f = open(filepath, "w")
# "r+" read and write
#'a+'append and read
# f.read()
f.write(f"{today_date.day}/{today_date.month}/{today_date.year}")
f.writelines(["Hello", "World"])
f.close()
# Exercise 3
cars_file = "cars.txt"
f2 = open(cars_file, 'r')

lines = f2.readlines()
count = 0
for line in lines:
    line = line.strip()
    if len(line) >= 6:
        print(line)
        count +=1
print(count)

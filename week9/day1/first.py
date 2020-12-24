# import secondary
#
# print("Hey, I'm first.py")
# print("Name of the first.py is:", __name__)
# #replaced = replace_letter("I love python", "x", "o")
# # print(secondary.replaced)
# # print(secondary.l)
# # print(secondary.count_obj)
# # print(secondary.count_obj)
#
# replaced = secondary.replace_letter("Hey, I'm first.py", "t", "o")
# import wikipedia
#
# search = wikipedia.search("Python")
# search1 = wikipedia.summary("Python(programming language)")
#
# first_search = search[1]
#
# print(search)
# print(first_search)
# print(search1)

# USEFUL MODULES
# RANDOM MODULES

# OS MODULES
# print(os.getcwd())
#
# for f in os.scandir():
#     print(f.path)
#     print(f.name)
# my_file = "secondary.py"
# print(os.path.abspath(my_file))
#
# file_path = "Users/desktop"

######TIME MODULE######
import time
before = time.time()

for i in range(1000000):
    i = i+1

after = time.time()
difference= after = before
print("The time is:", {difference})

time.sleep()

######DatETIME MODULE######
import datetime

today = datetime.datetime.now()
print("today:", today)

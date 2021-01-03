from function import new_name as nn
import random
nn("Svetlana")

#Exercise 2 Create a function that accepts a number between 1 and 100, then rolls a random number between 1 and 100,

user_num = int(input("Enter a number"))
def random_number():
    ran_number = random.randint(1,100)
    if user_num ==ran_number:
        print("You guess the number")
    else:
        print("You failed")
        i

random_number()

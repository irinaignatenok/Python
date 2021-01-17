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

#Exercise 3 Generate random String of length 5
import string
import random
def ranStr(chars = string.ascii_uppercase + string.ascii_lowercase, N=5):
  return ''.join(random.choice(chars)for _ in range(N))

print(ranStr())

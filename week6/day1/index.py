string = input("Please enter some information about yourself: ")

print(len(string))
if len(string) < 10:
    print("string not long enough”")
else:
    print("string too long")

#Exercise 2
#Then, print the first and last characters of the given text
print(string [0])
print(string [-1])
#Exercise 3
#Construct the string character by character: Print the first character, then the second, then the third, until the full string is printed
print(string [0])
print(string [0:2])
print(string[0:3])
print(string[:-1])
print(string[0:])

import random 

str = list("Hello world")
print(str)
random.shuffle(str)
print(''.join(str))
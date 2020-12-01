my_text = '''
Lorem ipsum dolor sit amet,consectetur adipiscing elitsed 
do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamcolaboris 
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
pariatur. Excepteur sint occaecat cupidatat non proident, sunt in 
culpa qui officia deserunt mollit anim id est laborum.
'''
print(len(my_text))

#Exercise 5: Longest Word Without A Specific Character
sentence = input("Please write a long sentence without letter a: ")
sentence.lower()
letter_a = sentence.find("a")
print(letter_a)
if letter_a == -1:
   print("congratulation!")
else:
   input("Try again")
   

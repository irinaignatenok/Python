#Print the following output in one line of code:
#Hello world
#Hello world
#Hello world
#Hello world
print("Hello world \nHello world \nHello world\nHello world ")

#Exercise2
#(99^3) * 8
print((99^3) * 8)


#Exercise 3 : What Is The Output ?
#Predict the output of the following code snippets:
 5 < 3 #False
3 == 3 #True
3 == "3" #True
"3" > 3 #False
"Hello" == "hello" #False

#Exercise 4 : Your Computer Brand
computer_brand = "macbook_air"
print(f"I have a {computer_brand} computer")

#Exercise 5: Your Information
name = "Irina"
age  = 30
shoe_size = 39
info = f"Hi my name is Irina, I live in Tel Aviv.I am {age} years old.Unfortunately I have a {shoe_size} shoe size"
print(info)

#Exercise 6: Odd Or Even
#Write a script that asks the user for a number and 
#determines whether this number is odd or even.
number = int(input("Please,enter a number: "))
if (number%2 == 0):
    print("The number is even")
else:
    print("The number is odd")

#Exercise 7 : What’s Your Name ?

#Write a script that asks the user for his name and determines 
#whether or not you have the same name, 
#print out a funny message based on the outcome
my_name = "Sarah"
name = input("Please, write me your name: ")
if name == my_name:
    print("You stole my name...")
else:
    print(f"Actually, the name {my_name} would suit you")

#Exercise 8 : Tall Enough To Ride A Roller Coaster

#Write a script that will ask the user for their height 
#in inches, print a message if they can ride a roller 
#coaster or not based on if they are taller than 145cm
#Please note that the input is in inches and you’re 
#calculating vs cm, you’ll need to convert your data accordingly
#1 in = 2.54 cm
height = int(input("Please write your height in inches"))
print(height)
if (height/2.54) > 145:
    print("You can ride a roller coaster")
else:
    print("Unfortunately You're not tall enought")

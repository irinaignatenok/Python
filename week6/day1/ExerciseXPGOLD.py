#Print the following output in one line of code:

words = ("Hello world \n")*4
add_words = ("I love python \n")*4
print(f"{words}{add_words}")
#OR 
print("Hello world \n" *4 + "I love python \n" *4)

#Exercise 2 : What Is The Season ?
month = int(input("Please write your month of birth: "))
if 3 <= month <=5:
    print("You were born in spring")
elif 6 <= month <= 8:
     print("You were born in  summer")
elif 9 <= month <=11:
    print("You were born in autumn")
elif 12<= month <= 2:
    print("You were born in winter")
else:
    print("Incorrect number")
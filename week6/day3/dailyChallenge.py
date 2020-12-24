my_fav_numbers = {2,5,7,9}
#add number
my_fav_numbers.add(8)
print(my_fav_numbers)

#remove the last number
my_fav_numbers.remove(9)

#create a new set
friend_fav_numbers = {56, 78, 33, 5, 7}

#concatenate two sets
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

#Exercise 3: Print A Range Of Numbers

for number in range(1,21):
    print(number)

#Exercise 4 Float
import decimal

def float_range(start, stop, step):
  while start < stop:
    yield float(start)
    start += decimal.Decimal(step)
new_float = list(float_range(1, 5.5, '0.5'))
new_float.pop(0)
print(new_float)

#Exercise 5 

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
#remove item
basket.remove("Banana")
basket.remove("Blueberries")
#add item
basket.insert(2, "Kiwi")
basket.insert(0, "Apples")
#count item
nb_of_apples = basket.count("Apples")
print(nb_of_apples)
#clear
basket.clear()
print(basket)

#Exercise 6 Loop
#Write a while loop that will keep asking the 
#user for input until 
#the input is the same as your name.
name = "Irina"
name1 = ""
name_input = input("What's your name: ")
while name_input != name:
  name1 = input("What's your name: ")
  if name1 == name:
    print("We have the same name")
    break
print("stop looping")

#Exercise 7

#Given a list, use a while loop to print out 
#every element which has an even index.
my_list = [2,5,6,8,3,66,55,45,23]

res = []
for i, num in enumerate(my_list):#I used for loop
  if i %2 ==0:
    res.append(num)
print(res)

#Exercise 8
#Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.

res = []

for i in range(3, 31):
  if i % 3 == 0:
    res.append(i)
print(res)

#Exercise 9 
#Use a for loop to find numbers between 1500 and 2700, 
#which are divisible by 7 and multiples of 5.

res = []

for i in range(1500, 2700):
    if i % 7 == 0 and i % 5 == 0:
        res.append(i)
print(res)

#Exercise 10: Favorite Fruits

fruits = input("What's your favorite fruits(please separate the fruits with single space)?: ")
list(fruits)
#','.join(list_of_fruits)
#print(type(''.join(list_of_fruits)))

# Now that we have a list of fruits, ask the user to type in the name of any fruit.
name_of_fruit = input("please type the name of any fruit.: ")
if name_of_fruit in fruits:
    print("You chose one of your favorite fruits! Enjoy!")
elif name_of_fruit not in fruits:
    print("You chose a new fruit. I hope you enjoy it too!: ")
else:
    print("You have an error")

# Exercise 11
family = [["Rick", 59], ["Morty", 13], ["Summer", 21], ["Beth", 42]]

total_price = []
for member in family:
    members = member[1] #You called this variable members, but what does it contain ? nothing before my code didn't work
    #it was an error something with str and int
    # print(members)

#     # Try to print the name and the age, without another looping. THANKS!!!!
    if members < 3:
        price =o
        total_price.append(price)
    elif 3 <= members <=12:
        price = 10
        total_price.append(price)
    else: 
         price = 15
         total_price.append(price)
print(sum(total_price))


# Exercise 12
# Write a loop that prompts the user to enter a 
# series of pizza 
# toppings until they enter a ‘quit’ value.

pizza_toppings = input("Please add pizza toppings in the and write quit")



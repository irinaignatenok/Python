keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
for key,value in zip(keys, values):
  print(f"{key}:{value}")

  #Exercise 2 
#   Using a for loop, the dictionary above, and the instructions,
#  print out how much each family member will need to pay alongside their name
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
my_dict = {}
total = 0
for elem in family:
  
  if family[elem] < 3:
    my_dict.update({elem: 0}
    )
    total+=0
  elif 3 <=family[elem] <= 12: 
     my_dict.update({elem: 10})
     total+=10
  else:
    my_dict.update({elem: 15})
    total+=15
print(my_dict, "total:", total)


# Bonus: let the user input the names and ages instead of 
# using the provided family variable (Hint: ask the user 
# for names and ages and add them 
# into a family dictionary that is initially empty)
name = input("What's your name: ")
age = input("How old are you?: ")
family = {}
family.update({name:age})
print(family)

# Exercise 3 
# 1task
# Create a dictionary called brand, and translate the information 
# above into keys and values.
brand = {
  "name": "Zara",
  "creation_data": "1975",
  "creator_name": "Amancio Ortega Gaona",
  "type_of_clothes": ["men","women", "children", "home"],
  "international_competitors": ["Gap", "H&M", "Benetton"],
  "number_stores": 7000,
  "major_color":["France -> blue", "Spain -> red", "US -> pink, green"]
}
# 1.Change the number of stores to 2.
brand["number_stores"] = 2
print(brand)
# 2.Print a sentence that explains who the clients of Zara are.
print(f"The clients of {name} are", brand["type_of_clothes"][0],
brand["type_of_clothes"][1],brand["type_of_clothes"][2])

# 3.Add a key called country_creation with a value of Spain to brand
brand["country_creation"] = "Spain"
print(brand)

# 4.If the key international_competitors is in the dictionary, add the store Desigual.
if "international_competitors" in brand.keys():
  brand["international_competitors"].append("Desigual")
  print(brand)

# 5.Delete the information about the date of creation.
del brand["creation_data"]
print(brand)

# 6.Print the last international competitor
print(brand["international_competitors"][-1])

# 7.Print in a sentence, the major clothes’ colors in the US.
print(f"The major clothes' color in US are",brand["major_color"][-1])

# 8.Print the amount of key value pairs (length of the dictionary).

print(len(brand))

# 9.Print only the keys of the dictionary.
print(brand.keys())

# 10.Create another dictionary called more_on_zara with the following information:
more_on_zara = {
"creation_date": 1975, 
"number_stores": 10000  
}

# 11.Use a method to add the information from the dictionary
brand.update(more_on_zara)
print(brand)
# Exercise4
users = ["Mickey", "Minnie", "Donald","Ariel","Pluto"]
num = [0,1,2,3,4]
for num, index in zip(users,num):
  print({num:index})

# 2
users = ["Mickey", "Minnie", "Donald","Ariel","Pluto"]
disney_users = sorted(users)
print(disney_users)
num = [0,1,2,3,4]
for num, index in zip(disney_users,num):
  print({num:index})

#   3
users = ["Mickey", "Minnie", "Donald","Ariel","Pluto"]
disney_users = sorted(users)

num = [0,1,2,3,4]
for elem, index in zip(disney_users,num):
  if elem.lower().startswith("m") or elem.lower().startswith("p"):
    print({elem:index})



birthday = {"Irina":"1990/09/16", "Tatyana": "1985/04/25",
"John": "1970/08/6",
"Mia":"1995/09/7",
"Rianna":"1993/10/18"}
for message in birthday:
  print(f"Welcome",message,"!","You can look up the birthday of the people in the list",birthday[message] )

# Ask the user to give you a person’s name and store his answer in a variable.
# Get the birthday for the person’s name from the birthdays dictionary.
birthday = {"Irina":"1990/09/16", "Tatyana": "1985/04/25",
"John": "1970/08/6",
"Mia":"1995/09/7",
"Rianna":"1993/10/18"}
name = input("What's your name? ")
for member in birthday:
  if name == member:
    print(birthday[member])
  else: 
    print("Your name is not in the list")
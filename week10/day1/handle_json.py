import json

my_family = {
    "Father": "Rick",
    "Mother": "Beth",
    "Children": ["Summer", "Morty"]
}

json.load # Load data from a file
json.dump # --> Save data onto a file

#Both files need a file object as argument
f = open("my_family.json", "w")
json.dump(my_family, f) #f needs to be an object
f.close

f = open("my_family.json", "r")
my_dict = json.load(f)
print(my_dict)
f.close()

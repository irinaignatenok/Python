import json

# menu = {
#     "dishes": [],
#     "first_plates": [],
#     "desserts": []
# }
#
# f = open("menu.json", "w")
# my_menu = json.dump(menu, f)
# f.close()

def add_to_menu(category, element):
    f = open("menu.json", "r")
    my_menu = json.load(f)
    f.close()
    my_menu[category].append(element)

    f= open("menu.json", 'w')
    json.dump(my_menu, f)

def remove_from_menu(category,element):
    f.open("menu.json", "r")
    my_menu = json.load(f)
    f.close()
    my_menu[category].remove(element)

    f= open("menu.json", 'w')
    json.dump(my_menu, f)

def fancy_menu_display():
    f = open("menu.json", "r")
    my_menu = json.load(f)
    f.close()
    print("Here is our menu:")
    for category, dishes in menu.items():
        print(f"Our {category}:")

        for dish in dishes:
            print(f"{dish}")

add_to_menu("dishes", "Fish")
add_to_menu("dishes", "Carrot")
fancy_menu_display()

class MenuItem():

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.all_items = []

    def __str__(self):
        return f"{self.name}{self.price}"

    def add_items_to_menu(self):
        self.all_items.append(self.name)
        self.all_items.append(self.price)
        print(self.all_items,self.name, self.price)
    def get_by_name(self, menu):
        if item in menu:
            print(f'{item.name}')


item = MenuItem('Burger', 35)
print(item.add_items_to_menu())
print(item)

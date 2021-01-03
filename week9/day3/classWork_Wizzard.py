class Character():

    def __init__(self, name, attack = 10):
        self.name = name
        self.life = 20

    def basic_attack(self, character):



class Druid(Character):

    def meditate(self):
        self.life = 20+10
        self.attack =self.attack - 2
        print(f"{self.life}{self.attack}")

    def animal_help(self):
        self.attack = self.attack + 5
        print(f"{self.attack}")

    def fight(self, other):
        self.other = self.other - (0.75* self.life)
        print(f"{self.other}")



class Justice(Character):

class SuperPower(Character):

char = Character("Druid")
char1 = Druid.animal_help(char)
print(char1)

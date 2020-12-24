class LivingThing():

    def __init__(self, name):
        self.name = name

    def breath(self):
        print("Breath")
    
    def eat(self):
        print("Eating...")

class Animal(LivingThing):

    def __init__(self,name, age):
        self.age = age
        self.name = name

    def move(self):
        print("Move")

    def eat(self):
        print("Eat")

cat = Animal("Leo",1) # Create an animal, not a living thing !

cat.breath()
cat.eat()



#EXercise
class Vehicle():

    def __init__(self, brand, max_speed, fuel_capacity, fuel_current): # Not like this
        self.brand = brand
        self.max_speed = max_speed
        self.fuel_capacity =           fuel_capacity
        self.fuel_current = fuel_capacity
        # Here: self.fuel_current = fuel_capacity Ok thanks
        # Fuel current shouldn't be a parameter, it should be equal to the capacity at the beginning 

    def travel(self, distance):
        print(f"Travelling {km} km")
        self.fuel_current -= distance/10
    
    def fill_up_fuel(self):
       self.fuel_current = self.fuel_capacity


class Car(Vehicle):

    def carry(self,weight):
        if weight > 100:
            print("weight exceeded")
        else:
            print("Carry")

class Truck(Vehicle):

    def carry(self, weight):
        if weight >10000:
            print("Weight exceedee")
        else:
            print("Carry")

class Motorcycle(Vehicle):

    def travel(self, distance):
        print(f"Travelling {distance}km")
        self.fuel_current -= distance/50


# Exercise 3

class Hero(): # The parameters should not be here they should be in the __init__ function yessss
    def __init__(self, name)
        self.name = name
        self.level = 1 # Those variables will be destroyed at the end of the function, they are not part of self
        self.xp_count = 0

    def describe(self):
        print(f"The name of the hero is {self.name.title()}, the level is {self.level}") 
    def level_up(self):
        self.level +=1
        self.xp_count = 0

    def gain_xp(self, amount):
        self.xp_count += amount
        if self.xp_count > 100:
            self.level_up
            # Level up !to print it?
            # No, actually increment self.level by one ..OK
    
    def fight_monster(self):
        print(f"Fighting a monster")
        self.gain_xp(10)
        
        # class Vehicle():

#     def __init__(self, brand, max_speed, fuel_capacity, fuel_current): # Not like this
#         self.brand = brand
#         self.max_speed = max_speed
#         self.fuel_capacity =           fuel_capacity
#         self.fuel_current = fuel_capacity
#         # Here: self.fuel_current = fuel_capacity Ok thanks
#         # Fuel current shouldn't be a parameter, it should be equal to the capacity at the beginning 

#     def travel(self, distance):
#         print(f"Travelling {km} km")
#         self.fuel_current -= distance/10
    
#     def fill_up_fuel(self):
#        self.fuel_current = self.fuel_capacity


# class Car(Vehicle):

#     def carry(self,weight):
#         if weight > 100:
#             print("weight exceeded")
#         else:
#             print("Carry")

# class Truck(Vehicle):

#     def carry(self, weight):
#         if weight >10000:
#             print("Weight exceedee")
#         else:
#             print("Carry")

# class Motorcycle(Vehicle):

#     def travel(self, distance):
#         print(f"Travelling {distance}km")
#         self.fuel_current -= distance/50



class Hero(): # The parameters should not be here they should be in the __init__ function yessss
    def __init__(self, name, hit_power)
        self.name = name
        self.hit_power = hit_power
        self.level = 1 
        self.xp_count = 0
        self.life_points = 100

    def describe(self):
        print(f"The name of the hero is {self.name.title()}, the level is {self.level}") 
    def level_up(self):
        self.level +=1
        self.xp_count = 0

    def gain_xp(self, amount):
        self.xp_count += amount
        if self.xp_count > 100:
            self.level_up
            # Level up !to print it?
            # No, actually increment self.level by one ..OK
    
    def fight_monster(self, monster):
        self.loose_hp(monster.hit_power) 
        if self.is_alive:
            print(f"{self.name} won against {monster.name} !!")
            self.gain_xp(10)
        else:
            print(f"{self.name} lost at {monster.name}, too bad.")


    def loose_hp(self, amount):
        self.life_points -= amount
        if self.life_points <0:
            self.life_points = 0
    
    def add_hp(self, amount):
        self.life_points += amount
        if self.life_points > 100:
            self.life_points = 100

    def is_alive(self):
        if self.life_points > 0:
            return True
        else:
            return False




class Monster():
    def __init__(self, name, hit_power):
        self.name = name
        self.hit_power = hit_power
        self.life_point = 1000
    
    
class Drood(Hero):

    def heal(self, hero):
        hero.add_hp(20)

monster1 = Monster("Billy", 20)
monster2 = Monster("Mornclaw", 15)
monster3 = Monster("The Lean Being", 33)

player1  = Hero("Rick", 30)
player2  = Hero("Eyal", 50)
player3  = Hero("Joey", 1)

def battle(monsters, players):
    monsters = []
    players = []
    monster.append(moster1)
    monster.append(moster2)
    monster.append(moster3)

    players.append(player1)
    players.append(player1)
    players.append(player1)

    all_dead = False
    while all_dead == False or  len(monsters) == 0:

        all_dead = True
        for player in players:
            # Check if he is alive
            if not player.is_alive():
                continue
            
            if len(monsters) == 0:
                break

            all_dead = False
            monster = monsters.pop()
            player.fight_monster(monster)
    
    if len(monsters) == 0:
        print("Heroes won !")
    else:
        print("Monsters won !"))
    



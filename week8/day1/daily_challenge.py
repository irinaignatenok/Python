class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}
           
    def add_animal(self, animal, count =1):
        animal = animal.lower()
        if animal in self.animals:
            self.animals[animal] += count
        else:
            self.animals[animal] = count
            
    def get_info(self):
        
        msg = ''
        msg += f"{self.name}'s Farm'"
        msg += "\n\n"
        
        for animal, quantity in self.animals.items():
            msg += f"{animal}: \t{quantity}"
            msg += "\n"
        
        msg += "\n"
        msg += "\t\tE-I-E-I-O"
        return msg

      
macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())   

#EXercise

class Zoo():
    
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
        
    def add_animal(self, new_animal):
        if new_animal in self.animals:
            return False
        
        self.animals.append(new_animal)
     def sell_animal(self, animal_sold):
         if animal_sold in self.animals:
             self.animals.remove(animal_sold)
    
    def print_animals(self):
        for animal in self.animals:
            print(f" - {animal}")
            
    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        
        animals_index = {}
        current_letter = ""
        letter_index = 1
        for animal in sorted_animals:
            same_letter = []
            for animal_2 in sorted_animals:
                if animal[0] == animal_2[0]:
                    same_letter.append(animal_2)
            animal_index[INDEX] = same_letter
            letter +=1    
            
            current_letter = animal[0]  
        return animals_index
    def prinr_groups(self):
        
        groups = self.sort_animals()
        for animal in groups.values():
            
            for animal in animals:
                print("-", animal.title())  
                
            print('='*10)
    ramat_gam_safari = Zoo("Ramat Gan Safari")
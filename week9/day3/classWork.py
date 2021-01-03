class Task():

    def __init__(self, content, date):
        self.content = content
        self.date = date

    def __str__(self):
        return f"{self.content} {self.date}"

 class TodoList():

    def __init__(self, name):
        # name is the name of the list
        self.name = name
        self.list_of_tasks = []

    def add_task(self, task):
        # param task: Task to add to the list
        self.list_of_tasks.append(task)

    def display_list(self):
        print("Upcoming tasks:")
        for tasks in self.list_of_tasks:
            print(f"{tasks.date} {tasks.content}")

    def __len__(self):
        # Returning the length of the list of tasks
        return(self.list_of_tasks)


todo_list = TodoList("My TODO List")

task1 = Task("Learn python", "Saturday 26.12")
task2 = Task("Learn python", "Sunday 27.12")
task3 = Task("Learn python", "Monday 28.12")
task4 = Task("Clean the room", "Monday 31.12")

todo_list.add_task(task1)
todo_list.add_task(task2)
todo_list.add_task(task3)
todo_list.add_task(task4)

todo_list.display_list()
print(len(todo_list))


# Exercise 2



import random

class Car():

    # Class attribute (Not an object attribute)
    cars_count  = 0 # Count of all the cars created
    all_cars    = [] # List of all objects created

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

        # License number --> Index of creation of the car
        self.license_number = self.pad_license_number(Car.cars_count)

        # Increment the cars count
        Car.cars_count += 1

        Car.all_cars.append(self)

    def info(self):
        print(f"{self.brand} {self.model} N*{self.license_number}")

    # CLASS METHOD (!= instance method):
    @classmethod
    def generate_random_car(cls):
        """
        Generating a randomized car (random brand and random model)
        """
        brands = [
            "Dodge",
            "Genesis",
            "Hyundai",
            "Kia",
            "Land Rover",
            "Lexus",
            "Mazda",
            "McLaren"
        ]

        types = [
            "Hatchback",
            "Sedan",
            "SUV",
            "Crossover",
            "Coupe",
            "Convertible",
        ]

        random_car_brands = random.choice(brands)
        random_car_type = random.choice(types)
        car = cls(random_car_brands,random_car_type)
        return car

    @classmethod # --> Receives cls (representing the class itself) instead of self
    def find_car_by_id(cls, car_id):
        """
        Find a car given it's id
        :param cls: Reference class
        :param car_id: (str) license_number of the car

        return (Car) The car object that holds this id OR None if no car hold it
        """

        for car in cls.all_cars:
            if car.license_number == car_id:
                return car

        # If I reach this line --> No car was found --> Return None
        return None

    @staticmethod # --> Don't receive neither self nor cls
    def pad_license_number(license_number, final_len=8):
        """
        Padding the license number so it ends being a <final_len> digits string
        For example: 32 --> 00000032
        :param license_number: (str) Original number (Not padded)
        :param final_len: (int) The length of the final string (default is 8)
        """
        # Making sure that license_number is a string
        license_number = str(license_number)

        # What is the current number of digits ?
        current_digits = len(license_number)

        # How many zeros should I add on the left to get to final_len digits?
        fill_space = final_len - current_digits

        # Create my final string ("0" has to be a string, put quotes !)
        final_string = "0"*fill_space + license_number

        return final_string

for i in range(100000):
    Car.generate_random_car()
print("FInished")

my_car = Car.find_car_by_id("00012345")
my_car.info()
# car1 = Car("Toyota", "Yaris")
# car2 = Car("Porsche", "Cayenne")
# car3 = Car("Audi", "R8")
#
# car1.info()
# car2.info()
# car3.info()
#
# toyota = Car.find_car_by_id("00000000")

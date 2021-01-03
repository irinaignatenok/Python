class Currency:

    def __init__(self, currence_type, value):
        self.currence_type = currence_type
        self.value = value

    def __str__(self):
        return f"{self.currence_type} with value of {self.value}"

    def __repr__(self):
        return {"currence_type": self.currence_type, "value": self.value}

    def math_currency(self, another_currency, operator):

        if self.currence_type == another_currency.currence_type:

            if operator == "+":
                return self.value + another_currency.value
            elif operator == "-":
                return self.value - another_currency.value
            elif operator == "*":
                return self.value * another_currency.value
            elif operator == "/":
                return self.value / another_currency.value

        else:
            raise Exception("Can't match different values")

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)
str(c1)
int(c1)
repr(c1)
c1 + 5

# Exercise 3
from datetime import datetime
new_year = datetime(year = 2021, month = 1, day = 1, hour = 12)
countdown = new_year - datetime.now()
print(f"New year will come in {countdown} days")

# Exercise 4
from datetime import datetime
date_today = datetime.now()
new_year = datetime(year = 2021, month = 1, day = 1, hour = 00)
print(new_year)
holiday_coming = new_year - date_today
print(f"Holiday coming in {holiday_coming}")

# Exercise 5
from datetime import datetime

from datetime import datetime

def minutes_of_life(birthdate):
  date_today = datetime.now()
  life_minutes = (date_today - birthdate)
  return life_minutes

birthdate = datetime(year = 1990, month = 9, day = 26, hour = 5)
minutes_in_day = 1140
number_of_minutes = minutes_of_life(birthdate)*minutes_in_day
print(f"You have lived {number_of_minutes} in your entire life")

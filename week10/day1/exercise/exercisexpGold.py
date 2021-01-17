#Exercise1
# Create a function that displays the current date.
# Hint : Use the datetime module
import datetime

x = datetime.datetime.now()
print(x)

#Exercise2
# Create a function that displays a countdown to the next January 1st.
# import datetime
x1 = datetime.datetime.now()
def till_next_year():
  countdown = datetime.datetime(2022, 1, 1) - x1
  return countdown

print(till_next_year())

# Exercise 3
# Write a function that display today’s date, and a countdown to the next upcoming holidays.
def till_next_holiday(current_date, upcoming_date):
  countdown_to_holiday = upcoming_date - current_date
  return countdown_to_holiday

print(till_next_holiday(datetime.datetime.now(), datetime.datetime(2021, 2, 14)))

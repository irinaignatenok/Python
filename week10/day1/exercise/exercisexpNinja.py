# Exercise2
# Create an empty array of dictionnaries called user
# Use faker to add the keys name, adress, langage_spoken, and populate them with fake data


from faker import Faker
fake = Faker()
def create_date(x):
  user = {}
  for i in range(x):
    name = fake.name()
    language = ["english", "russian"]
    user["user_name"] = name
    user["user_language"] = language[0]
  return user

print(create_date(3))

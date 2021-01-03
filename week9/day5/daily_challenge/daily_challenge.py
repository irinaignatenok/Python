count = 0
name = []
age = []
score = []
while count < 5:
  count += 1
  names = input("enter your name: ")
  ages = str(int(input("enter age")))
  scores = str(int(input("enter score")))
  name.append(names)
  age.append(ages)
  score.append(scores)
print(name)
print(age)
print(score)

# Buil a list of tuples
combo = list(zip(name, age,score))
print(combo)
combo.sort(key = lambda name:name[1])
print(combo)
# na, ag, sc = zip(*combo)
# print(list(na),list(ag),list(sc))

import random


#functions
def compare(a, b, c, d):
  c = str(a)
  d = str(b)
  if a > b:
    print(c + " is greater than " + d)
  elif a < b:
    print(c + " is less than " + d)
  else:
    print(c + " is equal to " + d)

def eliminate(c, d):
  random.shuffle(c)
  for i in range(d):
    i = 0
    c.pop()
  return c
#lists
names = []

#the code
for i in range(3):
  i = 0
  integer1 = int(input("Enter an integer. "))
  integer2 = int(input("Enter another integer. "))
  compare(integer1, integer2, integer1, integer2)

for i in range(6):
  i = 0
  name = input("Enter a name. ")
  names.append(name)

vote = int(input("How many how many people would you like to vote off the island? "))
final = eliminate(names, vote)
print(final)

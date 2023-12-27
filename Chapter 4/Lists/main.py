#Welcome!
#A loop that will output every other name in the names list.

'''
Reflection:
Instead of having a ton of separate variables, everything can be found in one spot, and still be accessed. If every name and number were a different variable, then it would be much longer, harder to read, and harder to use. It's like a computer without folders for each respective file. 
'''




# DANNY AND CAROL WERE REMOVED AS A LIST IS MAX 99 CHARS
names = ['Peter', 'Bruce', 'Steve', 'Tony', 'Natasha', 'Clint', 'Wanda', 'Hope']
x = -1

while x < 3:
  x = x + 1
  names.pop(x)
print(names)

#A loop that will output only the positive numbers in the numbers list.
numbers = [100, 50, 10, 1, 2, 7, 11, 17, 53, -8, -4, -9, -72, -64, -80]
i = 0
while i < 6:
  i = i + 1
  numbers.pop(-1)
print(numbers)


#A loop that will output the sum of all the values in the numbers list.
numbers = [100, 50, 10, 1, 2, 7, 11, 17, 53, -8, -4, -9, -72, -64, -80]
i = -1
total = 0
while i < 14:
  i = i + 1
  total = total + numbers[i]
print(total)

#A loop that will output only the numbers that are odd.
numbers = [100, 50, 10, 1, 2, 7, 11, 17, 53, -8, -4, -9, -72, -64, -80]
i = 0
while i < 14:
  i = i + 1
  if numbers[i] % 2 == 1:
    print(numbers[i])

#A loop that will output only the names that come before "Thor" in the alphabet from the names list.
# DANNY AND CAROL WERE REMOVED AS A LIST IS MAX 99 CHARS
names = ['Peter', 'Bruce', 'Steve', 'Tony', 'Natasha', 'Clint', 'Wanda', 'Hope']
i = 0
while i < 7:
  i = i + 1
  if names[i] < "Thor":
    print(names[i])

#A loop that will find the maximum or minimum value in the numbers list. This algorithm requires an additional variable that is assigned to the first element in the list. Then, in a loop compare each element to the variable. If the element is > (for max) or < (for min), assign the variable to the element. After the loop, print the variable.
numbers = [100, 50, 10, 1, 2, 7, 11, 17, 53, -8, -4, -9, -72, -64, -80]
i = 0
max = numbers[0]
while i < 14:
  i = i + 1
  if numbers[i] > max:
    max = numbers[i]
print(max)

import math
import random

small = float(input("Enter in a small decimal number: "))
large = float(input("Enter in a large decimal number: "))
pi = float(math.pi)
radius = random.uniform(small, large)
volume = (4/3) * pi * (float(radius)**3)
print("The volume of a sphere with a radius of,", radius, ", is:", volume)



#Using those numbers as lower and upper bounds, randomly generate a decimal value between the two.
#Using the randomly generated number, calculate the VOLUME  of a sphere if it were to have that size radius. 
#Output the radius as well as the volume back to the user.


#V = 4/3 π r³
#V = (4/3) * pi * (r**3)
#V = (4/3) * pi * (float(large)**3)

#r = c / (2 * π)
#c = 2 pi r

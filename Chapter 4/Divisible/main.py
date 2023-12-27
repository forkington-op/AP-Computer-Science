
name = input("Please enter your name. ")
integer_1 = int(input(name + ", input an integer. "))
integer_2 = int(input( name + ", input another integer. "))
int1 = str(integer_1)
int2 = str(integer_2)
quotient = integer_1/integer_2 

if (quotient % 1 == 0 and quotient >= 0):
  print(int1 + " is divisible by " + int2 + ".")
else:
  print (int1 + " is not divisible by " + int2 + ".")

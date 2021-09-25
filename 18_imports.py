# import math

# # We already know that we can import things into python, like the Python
# #  standard library. Let's start with the math module which contains a lot
# # of useful math tools.
# # Let's calc the area of a circle where r = 5, remember Pi r squared 
# print (math.pi * 5 ** 2) # 78.53981633974483

# # Let's try some math functions. There's a handy one called fsum which is for
# # adding together floating ints. We can use the regular old sum but we can get
# # some weird numbers, check this out.
# numbers = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
# print(sum(numbers))  # 0.9999999999999999
# numbers = [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]
# print(sum(numbers))  # 1.9999999999999998
# # Let's try this with fsum!

# numbers = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
# print(math.fsum(numbers))  # 1.0
# numbers = [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]
# print(math.fsum(numbers))  # 2.0

# Neato

# We can also import specific things from modules. Say if we only needed the pi
# constant from the math module. There's no problem with...
# import math
# and then just using math.pi, OR we could just use pi rather than math.pi. How?
# We could simply write...
# from math import pi
# Or if we wanted tau also?
# from math import pi, tau
# We could reference pi and tau directly rather than math.pi and math.tau
# What can we not do? from math import fsum, and we also could not use fsum if 
# we had JUSt imported pi or tau. This is pretty important to remember, but it's
# also important to remember that some modules there are certain things we can
# only access through this specific import syntax

# One exaxmple is tkinter because we want an app with a GUI. The tkinter lib 
# includes themed widgets that we can use in our apps, but in order to use them 
# we have to import ttk from the tkinter module. In this case, we must then:
# from tkinter import tkk

# So what happens when we import a module?
# 1. When we import an entire module Python runs the module and creates a module
# object so that we can access the things inside of it -- hence the dot 
# notation.
# 
# What else can we do? We can also alias our imports. Say we wanted to do some 
# data analysis and needed numpy. It's common convention when importing 
# something like numpty and to use np as syntax. We can accomplish this with 
# the following import statement:
# import numpy as np
# 
# In addition to aliasing we can also import using *
# from math import *
# That import statement would mean: Give me everything in the math module. 
# This, however, is not an import style we should be using 99% of the time. The 
# reason is that all of the names defined in the module we're importing are 
# going to get added to the global namespace. This can easily lead to name 
# conflicts.  

# EXERCISES
# 1) Import the fractions module and create a Fraction from the float 2.25. You
#  can find information on how to create fractions in the documentation.

# from fractions import Fraction
# from decimal import Decimal

# print(Fraction(Decimal('2.25')))

# Teclado's solution:
# import fractions
# fraction = fractions.Fraction(2.25)
# print(fraction)

# 2) Import only the fsum function from the math module and use it to find the 
# sum of the following series of floats:

# from math import fsum

# numbers = [1.43, 1.1, 5.32, 87.032, 0.2, 23.4]
# print(fsum(numbers)) # 118.482


# 3) Import the random module using an alias, and find a random number between 
# 1 and 100 using the randint function. You can find documentation for this 
# function here.

import random as rn

random_int = rn.randint(1, 100)
print(random_int)

# 4) Use the randint function from the exercise above to create a new version 
# of the guessing game we made in day 8. This time the program should generate 
# a random number, and you should tell the user whether their guess was too 
# high, or too low, until they get the right number.

target_number = 47

guess = int(input("Enter a number: "))
while guess != target_number:
  if guess > target_number:
    print("Wrong! Too High!")
    guess = int(input("Enter a number: "))
  else:
    print("Wrong! Too low!")
    guess = int(input("Enter a number: "))

print("That's right!")
# Quick recap of comprehensions
# We only use a comprehension when we want to change something about the values 
# when we make this new collection. For example, we might want to turn every 
# string in a list to title case:
names = ['tom', 'dick', 'harry']
names = [name.title() for name in names]
# Tom, Dick, Harry

# What if we want the names list to be a set?
names = ['tom', 'dick', 'harry']
names = set(names)

# We don't have to bother with the more verbose version
names = ['tom', 'dick', 'harry']
names = {name for name in names}
# With this in mind, we can really think of comprehensions as a way of 
# performing an action for every item in some iterable, and then storing the 
# results.

# The MAP FUNCTION!
# map is a function that allows us to call some other function on every item in 
# an iterable. Let's say we want to cube EVERY NUMBER in a list of numbers. 
# What can we do? Use map().
def cube(number):
  return number ** 3

numbers = [1,2,3,4,5,6,7,8,9]
cubed_numbers = map(cube, numbers)
# notice we pass in cube and not cube()
# if we try to print cubed_numbers, we'll just get its location in memory.
# <map object at 0x.....>
# This is because map objects are a lazy type, like zip enumerate or range.
# So how do we get something out of a map object? Iterate.
for number in cubed_numbers:
  print(number)

# Since they're an iterable, we can also unpack them using *
def cube(number):
  return number ** 3

numbers = [1,2,3,4,5,6,7,8,9]
cubed_numbers = map(cube, numbers)

print (*cubed_numbers, sep=", ")

# or we can convert them to a normal collection
def cube(number):
  return number ** 3

numbers = [1,2,3,4,5,6,7,8,9]
cubed_numbers = list(map(cube, numbers))

# Map with multiple iterables
# One nice thing about map is that we can handle several iterables at once.
def add(a, b):
	return a + b

odds = [1, 3, 5, 7, 9]
evens = [2, 4, 6, 8, 10]

totals = map(add, odds, evens)
print(*totals, sep=", ")  # 3, 7, 11, 15, 19
# If the iterables of are differing lengths, map will stop as soon as it runs 
# out of values, much like when using zip.

# map with lambda expressions
# map is frequently used for simple operations, which means it's often not 
# worth defining a full blown function.
# Lambda expressions are often used instead because they allow us to define a 
# function inline while calling map.
# 
# Let's cube again!
numbers = [1,2,3,4,5,6]
cubed_numbers = map(lambda number: number ** 3, numbers) 
# Easy and nice

# THE OPERATOR MODULE
# While lambda expressions are great, we often end up using lambda expressions 
# to duplicate the functionality of some operator. For example:
# lambda number: number ** 3 is just a way of using the ** operator on each 
# value.

# Since this kind of lambda expression is so common, there's a module in the 
# standard library called OPERATOR which contains function versions of all the 
# operators. It also includes some functions for making it easy to call methods 
# or access values in collections.

# Let's revisist our add function.
def add(a, b):
  return a + b

odds = [1,3,5,7,9]
evens = [2,4,6,8,10]
totals = map(add, odds, evens)
print(*totals, sep=", ") # 3, 7, 11, 15, 19

# We could easily do this as a lambda
odds = [1,3,5,7,9]
evens = [2,4,6,8,10]
totals = map(lambda a, b: a + b, odds, evens)
print(*totals,  sep=", ")
# while this is messy and not as clear as writing add, we don't necessary need 
# to define the add function even if we don't have to -- which we don't really 
# need to do. However, operator also already has an add function!

from operator import __add__
odds = [1, 3,5,7,9]
evens = [2,4,6,8,10]
totals = map(add, odds, evens)
print(*totals, sep=", ")

# Another useful function from operator is methodcaller. methodcaller allows us 
# to easily define a function that calls a method for us. We just have to 
# provide the method name as a string. Let's use our old friend title()
from operator import methodcaller
names = ['tom', 'dick', 'harry']
title_names = map(methodcaller("title"), names)
# or to lambdafy it
title_names = map(lambda name: name.title(), names)
# not as clear as our method

# CONDITIONAL COMPREHENSIONS
# We can use comprehension for more than just performing an action for each 
# item in an iterable, we can also perform filtering with comprehensions!

# We can do this by providing a condition at the end of our comprehension, and 
# this condition determines whether or not an item makes it into our new 
# collection. In cases where the condition evalues to True, the item is added; 
# otherwise it is discarded.

# Let's say we have a set of numbers and we only want the even values, let's 
# use a conditional comprehension to accomplish this.
numbers = [1, 56, 3, 5, 24, 19, 88, 37]
even_numbers = [number for number in numbers if number % 2 == 0]
# this is the same as the following:
even_numbers = []
for number in numbers:
  if number % 2 == 0:
    even_numbers.append(number)
# We can do this filtering operation with any kind of comprehension! Let's do 
# the same thing for set comprehension!
numbers = [1,56,3,5,24,19,88,37]
even_numbers = {number for number in numbers if number % 2 == 0}

# THE FILTER FUNCTION
# Much like map is a functional anaologue for 'normal' comprehensions, filter 
# performs the same role as a conditional comprehension. 

# Much like map, filter calls a function (known as a predicate) for every item 
# in an iterable, and it discards any values for which that function returns a 
# falsy value.

# A predicate is a function that accepts some value as an argument and returns 
# either True or Falsnumbers = [1, 56, 3, 5, 24, 19, 88, 37]
numbers = [1, 56, 3, 5, 24, 19, 88, 37]
even_numbers = filter(lambda number: number % 2 == 0, numbers)
# In this case we don't have an easy solution available in the operator module 
# - though there is a mod function - so we have to use etiher a lambda or we 
# define a function to call.

def is_even(number):
  return number % 2 == 0
numbers = [1, 56, 3, 5, 24, 19, 88, 37]
even_numbers = filter(is_even, numbers)

# Just like map, filter gives us a lazy filter object so the values are not 
# calculated until we need them. However, UNLIKE map, filter can only handle a 
# SINGLE ITERABLE AT A TIME. Not a big problem, but something to be aware of. 

# USING NONE WITH FILTER

# Instead of passing in a function to filter, it's possible to use None.
# This tells filter that we want to use the truth values of the values 
# directly, instead of performing some kind of comparison or calculation. In 
# this case, filter will keep all truthy values from the original iterable, and 
# all falsy values will be discarded.
values = [0, "Hello", [], {}, 435, -4.2, ""]
truthy_values = filter(None, values)
print(*truthy_values, sep=", ") # Hello, 435, -4.2

# EXERCISES
# 1) Use map to call the strip method on each string in the following list:

humpty_dumpty = [
	"  Humpty Dumpty sat on a wall,  ",
	"Humpty Dumpty had a great fall;     ",
	"  All the king's horses and all the king's men ",  
	"    Couldn't put Humpty together again."
]

print(*map(lambda line: line.strip(), humpty_dumpty), sep="\n")

# method caller version
print(*map(methodcaller("strip"), humpty_dumpty), sep="\n")
# Print the lines of the nursery rhyme on different lines in the console.

# Remember that you can use the operator module and the methodcaller function 
# instead of a lambda expression if you want to.

# 2) Below you'll find a tuple containing several names:

names = ("bob", "Christopher", "Rachel", "MICHAEL", "jessika", "francine")

# Use a list comprehension with a filtering condition so that only names with 
# fewer than 8 characters end up in the new list. Make sure that every name in 
# the new list is in title case.
names = [name.title() for name in names if len(name) < 8]

# 3) Use filter to remove all negative numbers from the following range: range
# (-5, 11). Print the remaining numbers to the console.
print(*filter(lambda number: number >= 0, range(-5, 11)))
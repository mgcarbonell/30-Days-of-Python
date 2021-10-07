# What are exceptions?
# Those errors we get: SyntaxError, NameError, TypeError

# Ask for permission vs asking for forgiveness
# Let's say we have an input and we want the user to input a digit (1,2,3) 
number = int(input("Please enter a whole number: "))
# but they instead write something like "Three." Rather than crash the entire 
# program, we could do something else.
while True:
  user_number = input("Please enter a whole number: ")

  if user_number.isnumeric():
    number = int(user_number)
    break
  else:
    print("You did not enter a valid integer!")


# slight problem here, however, is that if we pass in a negative we'll receive 
# an error. So we'll need to strip the initial - but we should use lstrip
# because lstrip only removes the characters from the LEFT SIDE of the string.

while True:
  user_number = input("Please enter a whole number: ")

  if user_number.lstrip('-').isnumeric():
    number = int(user_number)
    break
  else:
    print("You did not enter a valid integer!")
# However is we enter --3 we'll get an error.
# We would have to keep modifying our code to handle edge cases, and it can be 
# difficult to know if we've missed something until we encounter it. This 
# approach is called "Asking for permission." We're checking if something can
# be done in advance, and proceed if we determine that there aren't going to be
# many problems.

# This is not the approach to exception handling that we take in Python. In 
# Python, the preferred approach is to simply attempt what we think may fail, 
# and then to recover from an exception if one occurs. This turns the problem 
# into a much simpler one: knowing what exceptions might occur. In the case 
# above, we only need to worry about one exception: ValueError.

# ENTER THE TRY STATEMENT!

while True:
  try:
    number = int(input("PLease enter a whole number: "))
    break
  except ValueError:
    print("You did not enter a valid integer!")

# Our except clause is waiting to see if any ValueError is raised while we're 
# running these operations in the try clause. If a ValueError is raised, we 
# abandon the code in the try clause and we perform the actions listed in this 
# except clause instead.

# Small note: What happens if we get a TypeError instead? Our except clause is
# not going to handle it, so a TypeError will still terminate our program., but
# that can sometimes be what we want. 

# Important
# An important thing to keep in mind is that the try block is going to stop 
# running as soon as an exception occurs. If something goes wrong, it's as if  
# none of the code in the try block ever ran.

# Let's try handling multiple errors
import math

def averages(numbers):
  try:
    mean = math.fsum(numbers) / len(numbers)
    print(mean)
  except ZeroDivisionError:
    print(0)
  except TypeError:
    print("You provided invalid values!")

# Do we have to do multiple except blocks? If we are handling the multiple 
# errors DIFFERENTLY. If they are being handled the same, yes we can!
def average(numbers):
	try:
		mean = math.fsum(numbers) / len(numbers)
		print(mean)
	except (ZeroDivisionError, TypeError):
		print("An average cannot be calculated for the values you provided.")

# Lastly we can put in a bare except clause, and it will catch any exceptions
# that could occur.

def average(numbers):
	try:
		mean = math.fsum(numbers) / len(numbers)
		print(mean)
	except:
		print("An average cannot be calculated for the values you provided.")

# ELSE
# In addition to the try and except clauses we also have the else clause. The 
# code under the else clause only runs if no exceptions occur while executing 
# the code in the try clause.

def average(numbers):
	try:
		mean = math.fsum(numbers) / len(numbers)
	except ZeroDivisionError:
		print(0)
	except TypeError:
		print("You provided invalid values!")
	else:
		print(mean)


# FINALLY
# In addition to all those we have finally. Finally will ALWAYS RUN!!
# If an unhandled exception occurs, it doesn't matter. Finally will still run 
# its code before that exception terminates the program.
# If we return from a function inside the try statement, finally will interrupt # that return to run its own code first. You can see an example by running this # code:
def finally_flex():
	try:
		return
	finally:
		print("You return when I say you can return...")

finally_flex()

# This property is extremely useful for any situations where vital clean up is 
# required after an operation. An example is when working with files. What 
# happens if we encounter some problem while processing data in a file? We 
# still want to close the file when we're done, and with finally we can make 
# sure that this happens.

# Exercises
# 1) Create a short program that prompts the user for a list of grades 
# separated by commas. Split the string into individual grades and use a list 
# comprehension to convert each string to an integer. You should use a try 
# statement to inform the user when the values they entered cannot be converted.

user_input = input("Please enter a list of grades, separated by commas: ")
user_input.split(',')
try:
  grades = [int(grade) for grade in user_input]
except ValueError:
  print("The grades you netered were in an invalid format.")

#2) Investigate what happens when there is a return statement in both the try 
# clause and finally clause of a try statement.

def func():
  try:
    return "Returned from the try"
  finally:
    return "Returned from the finally"
print(func()) # Finally

#3) Imagine you have a file named data.txt with this content:

# There is some data here!

# Open it for reading using Python, but make sure to use a try block to catch 
# an exception that arises if the file doesn't exist. Once you've verified your 
# solution works with an actual file, delete the file and see if your try block 
# is able to handle it.

# When files don't exist when you try to open them, the exception raised is 
# FileNotFoundError.

try:
  with open ('data.txt', 'r') as file:
    print(file.read())
except FileNotFoundError:
  print("Error: could not find file.")
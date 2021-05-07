# Python only has 2 boolean values: True and False (note the capitalization)
# There are truthy values in python as well. We can find the truthy value of any value in Python by passing it to the bool function

print(bool("Hello"))  # => True
print(bool(0))  # => False
print(bool(1))  # => True
print(bool(""))  # => False
print(bool([0, 1, 2, 3]))  # => True
print(bool([]))  # => False

# In addition to bool we have the standard comparison operators < > =
print(5 < 10)  # => True
print(10 > 10)  # => False
print(0 == '0')  # => False
print(0 == 0)  # => True

# We also have a 'is not equal to' !=
print(0 != '0')  # => True

# there is also the `is` keyword, which checks to see if two things are exactly
# alike; or exactly the same thing.

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # => True
print(a is b)  # => False
print(a is a)  # => True

# We also have an id function which will tell us where something is stored in
# memory.

print(id(a))
print(id(b))

b = a
print(id(a))
print(id(b))
print(a == b)  # => True
print(a is b)  # => True
# notice that the is operator will work now, because they're stored in the same
# place in memory.

# So what are some applications of all of these if we tie them together?
name = input("Please enter your name: ")

if name:  # Checks the truthy value of the name by calling bool
    print(f"You entered {name}")
else:
    print("You did not enter anything.")

# EXERCISES:
# 1. Try to approximate the behaviour of the is operator using ==. Remember we # have the id function for finding the memory address for a given value, and we # can compare memory addresses to check for identity.

list_a = ['Hello', 'How', 'Are', 'You']
list_b = list_a
print(id(list_a) == id(list_b))

# 2. Try to use the is operator or the id function to investigate the
# difference between this:

# numbers = [1, 2, 3, 4]
# new_numbers = numbers + [5]
# And this:

# numbers = [1, 2, 3, 4]
# numbers.append(5)

numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]
print(id(numbers))  # 140294072877824
print(id(new_numbers))  # 140294072877952
print(numbers is new_numbers)  # False

numbers.append(5)
print(id(numbers))  # 140294072877952
print(numbers is numbers)  # True

# 3. Ask the user to enter a number. Tell the user whether the number is
# positive, negative, or zero.

number = int(input("What's your favorite number? "))
if number > 0:
    print(f"Your favorite number is {number}, a positive number")
elif number == 0:
    print(f'Is 0 even a number?')

else:
    print(f"Get real. Don't be so negative.")

# 4. Write a program to determine whether an employee is owed any overtime. You
# should ask the user how many hours the employee worked this week, as well as
# the hourly wage for this employee.

# If the employee worked more than 40 hours, you should print a message which
# says the employee is due some additional pay, as well as the amount due. The
# additional amount owed is 10 % of the employees hourly wage for each hour
# worked over the 40 hours. In effect, the employees get paid 110 % of their
# hourly wage for any overtime.

hours_worked = int(input("How many hours did you work this week? "))
hourly_wage = int(
    input('How much do you get paid hourly? Please enter a whole number: '))
if hours_worked > 40:
    overtime = (hourly_wage * 110) / 100
    print(f'You worked over 40 hours, your hourly wage should be {overtime}')

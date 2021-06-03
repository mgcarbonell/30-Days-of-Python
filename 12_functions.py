# How do we write functions in python? We use def.
# So rather than doing something like...
for number in range(1, 11):
    print(number * 2)

# we can go...


def get_even_numbers():
    for number in range(1, 11):
        print(number * 2)


get_even_numbers()
# print(get_even_numbers())

# but what if I want to make this more dynamic?
# we can pass arguments,parameters


def get_even_numbers_again(amount):
    for number in range(1, amount + 1):
        print(number * 2)


get_even_numbers_again(10)
# Cool

# FUNCTION PARAMETERS AND ARGUMENTS
# We know we can pass in arguments, and there are some functions we have to pass arguments, for example we can't just run len() it'll return an error. We can even pass multiple parameters


def x_print(requested_output, quantity):
    for _ in range(quantity):
        print(requested_output)


x_print("Hello!", 5)  # => print "Hello!" five times
# does the same, but here's a trick
x_print(requested_output="Hello", quantity=5)
# if we do x_print(5, "Hello!") we'll get an error, but if we do the above on line 39 and swap it...
x_print(quantity=5, requested_output="Hello!")
# that works just fine!
# x_print(5, requested_output="Hello!")  this, however does not.
x_print("Hello!", quantity=5)  # but this would


# Exercises
# 1) Define four functions: add, subtract, divide, and multiply. Each function should take two arguments, and they should print the result of the arithmetic operation indicated by the function name.

# When orders matters for an operation, the first argument should be treated as the left operand, and the second argument should be treated as the right operand. For example, if the user passes in 6 and 2 to subtract, the result should be 4, not -4.

# You should also make sure that the user can’t pass in 0 as the second argument for divide. If the user provides 0, you should print a warning instead of calculating their division.

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def divide(x, y):
    if(y > 0):
        return x / y
    else:
        return "No dividing by 0!"


def multiply(x, y):
    return x * y


print(add(2, 3))
print(subtract(3, 2))
print(divide(6, 2))
print(divide(6, 0))
print(multiply(2, 3))

# 2) Define a function called print_show_info that has a single parameter. The argument passed to it will be a dictionary with some information about a T.V. show. For example:

tv_show = {
    "title": "Breaking Bad",
    "seasons": 5,
    "initial_release": 2008
}

# The print_show_info function should print the information stored in the dictionary, in a nice way. For example:

#  Breaking Bad (2008) - 5 seasons
# Remember you must define your function before calling it!


def print_show_info(show):
    return f"{show['title']} ({show['initial_release']}) - {show['seasons']} seasons"


print(print_show_info(tv_show))

# 3) Below you’ll find a list containing details about multiple TV series.

series = [
    {"title": "Breaking Bad", "seasons": 5, "initial_release": 2008},
    {"title": "Fargo", "seasons": 4, "initial_release": 2014},
    {"title": "Firefly", "seasons": 1, "initial_release": 2002},
    {"title": "Rick and Morty", "seasons": 4, "initial_release": 2013},
    {"title": "True Detective", "seasons": 3, "initial_release": 2014},
    {"title": "Westworld", "seasons": 3, "initial_release": 2016},
]
# Use your function, print_show_info, and a for loop, to iterate over the series list, and call your function once for each iteration, passing in each dictionary. You should end up with each series printed in the appropriate format.


for show in series:
    print(print_show_info(show))

# 4) Create a function to test if a word is a palindrome. A palindrome is a string of characters that are identical whether read forwards or backwards. For example, “was it a car or a cat I saw” is a palindrome.


def palindrom_check(string):
    # if(len(string) == 0):
    #     print(False)
    string = string.strip().lower()
    reversed_string = reversed(string)

    if list(string) == list(reversed_string):
        print(True)
    else:
        print(False)


print(palindrom_check("Hannah"))

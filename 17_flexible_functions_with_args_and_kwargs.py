# Here we're going to talk about how to use the * and ** operators to make truly flexible functions that can accept ANY number of args.

# The problem:
# Several built in functions accept a variable number of args, for example
# look at print()
# print() can take an arbitrary number of positional arguments and it will
# print them all side by side by default. Print also controls these values with
# another parameter called sep which has a default vaul of " ". If we wanted to
# write something explicitly we could do...
# print(1, 2, 3, 4, 5, sep=" ") # 1 2 3 4 5
# However we're most familiar with something like print(1,2,3,4,5) # 1 2 3 4 5
# But we can't really replicate this, so how do we?
# Let's work with a multiply function

def mult(x, y):
    print(x * y)


mult(5, 10)  # 50
# now let's try this with an *
# First, let's be clear: * is actually an operator and not part of the
# parameter name. Generally speaking we call this special parameter: args
# which is sort for arguments (remember Java?)
# Let's use *args so we don't have to define x and y


def mul(*args):
    print(args[0] * args[1])


mul(5, 10)  # 50
# Another note: It's rare that we'd define a function as so, because *args
# means that it can accept ANY number of arguments. In the above, because we
# access args[0] and args[1] only it means we're really working with two
# variables and *args isn't really needed.
# Let's write a function with *args where it would make sense. Like a greeter:


def multigreet(*args):
    for name in args:
        print(f"Hello, {name}!")


multigreet("Rollo", "Raleigh", "Redford")
# To note: We use the name args not *args when defining the loop. Remember that
# * is just  an operator.

# Style note: Writing *args is very useful when the arguments can be anything,
# but in multigreet we have a very good idea of what the values represent:
# names. We could instead use *names and it would function just the same!


def multigreet(*names):
    for name in names:
        print(f"Hello, {name}!")


multigreet("Tom", "Dick", "Harry")
# Don't use *args if we have a better name. Remember that variable names are
# excellent tools for aiding in readability. Always use the most descriptive
# name you can.

# Parameter order with *args: IMPORTANT

# When we use a parameter like *args we have to be aware of the order of our
# parameters. Any parameters we define AFTER *args CANNOT accept positional
# arguments.
# In our multigreet had we done something like: def multigreet(*names, other)
# written the code the same and not called 'other' we would receive a TypeError
# of "missing 1 required keyword-only argument: other". So, instead, if we were
# to declare def multigreet(other, *names) and not called other we would avoid
# this error.
# Placing args after the * parameter can be very useful, we can force users to
# use keyword arguments for certain parameters. This can be useful for things
# we don't want the user to accidentally change, or things for which we have
# established defaults. To circle back print actually makes use of this with
# sep and end, which only accept keyword arguments.

# Accepting An Arbitrary Number of Keyword Arguments - IMPORTANT

# We know about positional arguments, now let's deal with any number of args.
# dict() makes use of this, let's try this out!
# dict(name="Phil", age=29, city="Budapest", nationality="British")
# Wild, the keywords become keys, and values we match become values
# That's the same as this:
# {
#   "name": "Phil",
#   "age": 29,
#   "city": "Budapest",
#   "nationality": "British"
# }
# dict did not know in advance how many keys and values we wanted to create our
# dictionary with, so it had to be flexible. We can achieve the same thing with
# another special parameter, this time with the ** in front of its name.
# Enter our new friend: **kwargs which is short for 'keyword arguments'


def pretty_print(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


pretty_print(title="The Matrix", director="Wachowski", year=1999)
# title: The Matrix
# director: Wachowski
# year: 1999

# Note that ** kwargs collects all unassigned keyword arguments and creates a
# dictionary with them, that you can then use in your function. That's why we
# have access to .items() in there, because kwargs is a dictionary.

# If we define both *args and **kwargs for a given function **kwargs MUST COME
# SECOND. If the order is reversed python says it's invalid syntax.

# **kwargs usually is and has to be the final parameter we define, because it
# has to come after *args as well as any other keyword arguments. It will gather
# up any remaining keyword arguments, so any parameters that come after it will
# never get provided a value.

# Other uses for * and **

# While we can use * and ** to gather up values into a single collection we can
# also use them in the opposite: unpacking an iterable into individual values.
# If you're fuzzy on this revisit day 9 and destructuring. However there's a key
# difference here: we were doing it in the context of assigning to a fixed
# number of variables. We simply matched the values provided by our iterable to
# the name number of variables and Python took care of the rest.
# What if this wasn't possible? What if we want to destructure an iterable so
# that we can pass many values to *args?

# We put a * before the iterable we're pass ing in as an argument.
# For example let's say I want to take this list of numbers and print the
# numbers on a single line with pipe ( | ) characters between each number.
# We could do the following:
numbers = [1, 2, 3, 4, 5]
print(*numbers, sep=" | ")  # 1 | 2 | 3 | 4 | 5

# Let's say we wanted to destructure a dictionary. We can do essentially the
# same except that by default Python gives us the keys when we iterate over
# a dictionary, so we need to use values or items when using *.


def print_movie(*args):
    for value in args:
        print(value)


movie = {
    "title": "The Matrix",
    "director": "Wachowski",
    "year": 1999
}

print_movie(*movie.values())
# The Matrix
# Wachowski
# 1999

# Were we to pass in *movie.keys() we'd get title, director, year

# We could also use ** to turn a dictionary into a series of keyword args.
# If we use **kwargs and dictionary destructuring we'd get something like:


def print_movie(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


movie = {
    "title": "The Matrix",
    "director": "Wachowski",
    "year": 1999
}

print_movie(**movie)
# title: The Matrix
# director: Wachowski
# year: 1999

# When we do **movie it turns the dictionary into keyword arguments. These are
# passed to print_movie, and the **kwargs parameter collects them back into a
# dictionary.

# While the above example could very easily be achieved as so:
# def print_movie(movie_details):
# 	for key, value in movie_details.items():
# 		print(f"{key}: {value}")


# movie = {
# 	"title": "The Matrix",
# 	"director": "Wachowski",
# 	"year": 1999
# }

# print_movie(movie)

# # title: The Matrix
# # director: Wachowski
# # year: 1999
# **kwargs gives us more flexibility when it comes to collecting unassigned
# keyword arguments, and not only those coming from the dictionary. What if we
# wanted to add a studio? We could with **kwargs!
print_movie(studio="Warner Bros", **movie)
# Here we used **kwargs to collect both the studio argument as well as all the
# movie arguments!

# How else can kwargs be used? When we merge dictionaries we don't need to use
# a ton of formatting. For example the day 14 project where we printed some
# output about books from alist of dictionaries we needed to do something like:
# print(f"{book['title]}, by {book['author]} ({book['year']})"). Instead of
# passing the f string we could have just use the format method with
# placeholders as so:
# print("{title}, by {author} ({year})".format(**book))
# This would create a series of keyword arguments from each book

# EXERCISES

# 1) Create a function that accepts any number of numbers as positional
# arguments and prints the sum of those numbers. Remember that we can use the
# sum function to add the values in an iterable.


def sum_a_lot(*numbers):
    print(sum(numbers))

# 2) Create a function that accepts any number of positional and keyword
# arguments, and that prints them back to the user. Your output should indicate
# which values were provided as positional arguments, and which were provided
# as keyword arguments.


def argument_printer(*args, **kwargs):
    print(f"Positional args: {args}")
    print(f"Keyword args: {kwargs}")

# Teclado's answer


def arg_printer(*args, **kwargs):
    args = [repr(arg) for arg in args]
    print(f"Positional arguments are: {', '.join(args)}")

    kwargs = [f"{key}={repr(value)}" for key, value in kwargs.items()]
    print(f"Keyword arguments are: {', '.join(kwargs)}")

# What is repr? Instead of using str() we can use the repr function which is
# going to give us a different kind of string representation (repr =
# representation) that aligns more with how we actually define the values. This
# is going to preserve the difference between 1 and "1".

# 3) Print the following dictionary using the format method and ** unpacking.


def print_country(**country):
    for key, value in country.items():
        print(f'{key.title()}: {value}')


country = {
    "name": "Germany",
    "population": "83 million",
    "capital": "Berlin",
    "currency": "Euro"
}

print_country(**country)

# Teclado's answer
country_template = """Name: {name}
Population: {population}
Capital: {capital}
Currency: {currency}
"""
print(country_template.format(**country))

# 4) Using * unpacking and range, print the numbers 1 to 20, separated by
# commas. You will have to provide an argument for print function's sep
# parameter for this exercise.

print(*range(1, 21), sep=", ")

# 5) Modify your code from exercise 4 so that each number prints on a different
# line. You can only use a single print call.
print(*range(1, 21), sep="\n")

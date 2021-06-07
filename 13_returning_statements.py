# Scope is a concept describing where a given name can be reference in our application.

# let's look at this for example:
def greet(name):
    greeting = f"Hello, {name}!"
    print(greeting)

# So we create the greeting variable within the function greet. Can we just print greeting like below?
# print(greeting)
# No, we will get a NameError that 'greeting' is not defined. Why? Because it was defined within the scope of the function named greet, and not globally. If we try to just print greeting, greeting is out of scope.

# Python actually keeps a record of the variables we've defined within a file, and the values that are associated with those names. We call this record a namespace, and you can think of it as being a dictionary. How cool is that? We can also access the globals with the globals() function.

# let's define some variables first:


names = ['Mario', 'Andy', 'Dan']
x = 349582


def add(a, b):
    print(a, b)


print(globals())
# What do we get back? A dictionary!
# {
#   '__name__': '__main__',
#   '__doc__': None,
#   '__package__': None,
#   '__loader__': < _frozen_importlib_external.SourceFileLoader object at 0x7f3108eabd60 > ,
#   '__spec__': None,
#   '__annotations__': {},
#   '__builtins__': < module 'builtins' (built-in) > ,
#   '__file__': '13_returning_statements.py',
#   '__cached__': None,
#   'greet': < function greet at 0x7f3108da5dc0 > ,
#   'names': ['Mario', 'Andy', 'Dan'],
#   'x': 349582,
#   'add': < function add at 0x7f3108db10d0 >
# }

# Hey neat! There's our greet function, our variables, and even our add function! But what's missing? our parameters a and b. What's going on? Well, we're looking at the GLOBALS output, and not the local output. So let's try this add again.


def add(a, b):
    print(locals())
    print(a, b)


add(7, 25)

# Very neat, we get back another dictionary again.
# {'a': 7, 'b': 25} okay so a, b are locals and not globals. This makes sense with what we're describing here. Nice!

# If whatever we define within a function stays within a function and we can't access it other places, how do we get a value out of the function? Let's use the RETURN statement!

# Return has two roles: first it executes the end of a function


def function_one():
    return
    print("This line will never be seen.")

# the print statement will never run because the return statement finishes the function. So what else does the return statement do? well we can return values.


def add(a, b):
    return a + b


result = add(5, 12)
print(result)  # => 17
print(add(12, 22))  # => 34

# Now let's take a look back at our greeting function.
print(greet('Phil'))
# We get:
# Hello, Phil! That's expected, but what's that next line?
# None
# None? What's going on. First, we get the result of calling the function, because Python needs to call the function to figure out what the value of greet('Phil') is. And then we print the return value of the function, which is None. The same thing will happen if we just have a function that's called and the return statement is just: return. So let's modify it.


def greet(name):
    greeting = f"Hello, {name}!"
    return greeting


print(greet('Phil'))
# Cool! We no longer have a None there. The value is no longer None, but now it's greeting. Coool.

# Can we have multiple return statements? You bet we can.


def divide(a, b):
    if b == 0:
        return "No dividing by 0!"
    else:
        return a / b

# How slick is that.

# Exercises
# 1) Define a exponentiate function that takes in two numbers. The first is the base, and the second is the power to raise the base to. The function should return the result of this operation. Remember we can perform exponentiation using the ** operator.


def exponent(a, b):
    return a ** b


print(exponent(5, 2))

# 2) Define a process_string function which takes in a string and returns a new string which has been converted to lowercase, and has had any excess whitespace removed.


def process_string(str):
    return str.strip().lower()


print(process_string("HeLlO THErE"))

# 3) Write a function that takes in a tuple containing information about an actor and returns this data as a dictionary. The data should be in the following format:

# ("Tom Hardy", "English", 42)  # name, nationality, age
# You can choose whatever key names you like for the dictionary.


def tuple_processor(tuple):
    data = {
        "name": "",
        "nationality": "",
        "age": ""
    }
    name, nationality, age = tuple
    data["name"] = name
    data["nationality"] = nationality
    data["age"] = age

    return data


print(tuple_processor(("Tom Hardy", "English", 42)))

# 4) Write a function that takes in a single number and returns True or False depending on whether or not the number is prime. If you need a refresher on how to calculate if a number is prime, we show one method in day 8 of the series.


def is_prime(n):
    if n < 2:
        return False

    for divisor in range(2, n):
        if n % divisor == 0:
            return False

    return True


print(is_prime(1))  # false
print(is_prime(2))  # true
print(is_prime(3))  # true
print(is_prime(4))  # false
print(is_prime(5))  # true
print(is_prime(6))  # false

# def get_grade_average(student):
#     return student["grade_average"]


# students = [
#     {"name": "Hannah", "grade_average": 83},
#     {"name": "Charlie", "grade_average": 91},
#     {"name": "Peter", "grade_average": 85},
#     {"name": "Rachel", "grade_average": 79},
#     {"name": "Lauren", "grade_average": 92}
# ]

# valedictorian = max(students, key=get_grade_average)
# print(valedictorian)
# {"name": "Lauren", "grade_average": 92}

# LAMBDA EXPRESSIONS
# alternative syntax for defining simple functions.
# Lambda expressions are EXPRESSIONS, and the value they evalute to is the
# function we want to create.

# In contract, the function defintions using the def keyword are statements.
# That means they do not have a value, which is why Python goes through the
# trouble assigning the function to a name for us. One major limitation of this
# is that we always have to define our functions separate from where want to
# use them.

# So what is a lambda? And how do we write it?
# First part of any lambda expression is the keyword: lambda
# We can also optionally specify any parameters for the function we want to
# create. Unlike regular fn defintions, these values are NOT put inside ().
# This section of the lambda expression is closed off with a colon : .
# After the colon comes an expression, and this expression is what we want to
# return from the function.

lambda a, b: a + b
# This is the same as:


def add(a, b):
    return a + b

# Let's look back to the get_grade_average that was used as a key for the max
# fn. If we wanted to write it as a lambda expression we could do so as follows:
# lambda student: student["grade_average"]
# Let's try our function again!


students = [
    {"name": "Hannah", "grade_average": 83},
    {"name": "Charlie", "grade_average": 91},
    {"name": "Peter", "grade_average": 85},
    {"name": "Rachel", "grade_average": 79},
    {"name": "Lauren", "grade_average": 92}
]

valedictorian = max(students, key=lambda student: student["grade_average"])
print(valedictorian)

# Another example of regular fn defintions vs lambdas. This little program will
# make a calcaultor:
# def add(a, b):
# 	print(a + b)


# def subtract(a, b):
# 	print(a - b)


# def multiply(a, b):
# 	print(a * b)


# def divide(a, b):
# 	if b == 0:
# 		print("You can't divide by 0!")
# 	else:
# 		print(a / b)


# operations = {
# 	"a": add,
# 	"s": subtract,
# 	"m": multiply,
# 	"d": divide
# }

# selected_option = input("""Please select one of the following options:

# a: add
# s: subtract
# m: multiply
# d: divide

# What would you like to do? """)

# operation = operations.get(selected_option)

# if operation:
# 	a = int(input("Please enter a value for a: "))
# 	b = int(input("Please enter a value for b: "))

# 	operation(a, b)
# else:
# 	print("Invalid selection")
# But we have so many defs. What if we did it this way instead?
def divide(a, b):
    if b == 0:
        return "You can't divide by 0!"
    else:
        return a / b


operations = {
    "a": lambda a, b: a + b,
    "s": lambda a, b: a - b,
    "m": lambda a, b: a * b,
    "d": divide
}

selected_option = input("""Please select one of the following options:

a: add
s: subtract
m: multiply
d: divide

What would you like to do? """)

operation = operations.get(selected_option)

if operation:
    a = int(input("Please enter a value for a: "))
    b = int(input("Please enter a value for b: "))

    print(operation(a, b))
else:
    print("Invalid selection")
# We can get away with 1 regular fn defintion (because of the if/else), and the
# rest of the pack is done via lambda expressions. Important to remember:
# LAMBDA EXPRESSIONS ARE LIMITED TO SINGLE EXPRESSIONS AND CANNOT CONTAIN
# STATEMENTS.


def add(a, b): return a + b


print(add(7, 8))

# EXERCISES
# 1) Use the sort method to put the following list in alphabetical order with
# regards to the students' names.

students = [
    {"name": "Hannah", "grade_average": 83},
    {"name": "Charlie", "grade_average": 91},
    {"name": "Peter", "grade_average": 85},
    {"name": "Rachel", "grade_average": 79},
    {"name": "Lauren", "grade_average": 92}
]

students.sort(key=lambda student: student["name"])
print(students)

# 2) Convert the following function to a lambda expression and assign it to a
# variable called exp.
# def exponentiate(base, exponent):
# 	return base ** exponent

# exp = lambda base, exponent: base ** exponent

# 3) Print the function you created using a lambda expression in previous
# exercise. What is the name of the function that was created?

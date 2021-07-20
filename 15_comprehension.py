# there are many types of comprehrension in python, but most commonly used is list comprehension.

# List comprehension is used to create a new list from some other iterable. It might be another list or even a zip object.

names = ["mary", "Richard", "Noah", "KATE"]

# Take a look at the names list and notice that they're not consistent.
# When can this happen? Grabbing data from a user.
# Let's make it all title case, we can interate over and create a new list.

processed_names = []

for name in names:
    processed_names.append(name.title())
# we would expect back a list of title case names: Mary, Richard, Noah, Kate
# While there's nothing wrong with this approach per se, we do create a new list and we can't simply get rid of our old list.
# It's potentially unncessary as well because we can just comprehension syntax!

processed_names = [name.title() for name in names]
# or we can just use... names
names = [name.title() for name in names]
# let's dissect this:
# In the above example the VALUE we want to ADD is name.title()
# The loop we have defined is `for name in names`
# Think of it like this: "Put name.title() in the new list for every name in names."

# Another example. We can have code like this:
names = ("mary", "Richard", "Noah", "KATE")
ages = (36, 21, 40, 28)
people = []

for name, age in zip(names, ages):
    person_data = (name.title(), age)
    people.append(person_data)

# OR we can rewrite this using COMPREHENSION

names = ("mary", "Richard", "Noah", "KATE")
ages = (36, 21, 40, 28)

people = [(name.title(), age) for name, age in zip(names, ages)]
# whew that looks cleaner.
# We would end up with: [('Mary', 36), ('Richard', 21), ('Noah', 40), ('Kate', 28)]

# SET COMPREHENSION
# This works just like list comprehesnion but produces a set rather than a list
names = ["mary", "Richard", "Noah", "KATE"]
names = {name.title() for name in names}
# => {'Mary', 'Richard', 'Noah', 'Kate'}

# DICTIONARY COMPREHENSION
# Like set comprehension, dictionary comprehensions are surrounded by curly bois {}

# Dict comprehension are a little different from list and set because dicts need both a key & a value. The syntax we use for the key value pair is the same as when we define a dictionary normally. First we have the key, followed by a ':' and then the value.

# Let's take a look. We used to do this:
student_ids = (112343, 134555, 113826, 124888)
names = ("mary", "Richard", "Noah", "KATE")

students = {}

for student_id, name in zip(student_ids, names):
    student = {student_id: name.title()}
    students.update(student)
#  => {112343: 'Mary', 134555: 'Richard', 113826: 'Noah', 124888: 'Kate'}

# OR we can produce the SAME dictionary when we do this:
student_ids = (112343, 134555, 113826, 124888)
names = ("mary", "Richard", "Noah", "KATE")

students = {
    student_id: name.title()
    for student_id, name in zip(student_ids, names)
}
# => {112343: 'Mary', 134555: 'Richard', 113826: 'Noah', 124888: 'Kate'}
# So to walk through: We have the value we want to add to our dictionary, our key value pair which is: student_id: name.title()
# This is followed by the loop definition which determines where the original values are comign from: for student_id, name in zip(student_ids, names)
# All of this is then placed within curly braces to indicate that we're using dictionary comprehension.

# COMPREHENSION AND SCOPE
# How does the scope work in comprehension?
names = ["Mary", "Richard", "Noah", "Kate"]
names_lower = []

for name in names:
    names_lower.append(name.lower())

print(name)  # This refers to the name variable we defined in the loop
# our output from the print statement is "Kate"
# If we tried to do this with name comprehension we would get a NameError because name is not defined. So what's going on here?

# Comprensions are actually just functions. When we define names_lower[name.lower() for name in names] we're actually writing something like follows:


def temp():
    new_list = []

    for name in names:
        new_list.append(name.lower())

    return new_list


# EXERCISES!

# 1) Convert the following for loop into a comprehension:

# numbers = [1, 2, 3, 4, 5]
# squares = []


# for number in numbers:
# 	squares.append(number ** 2)
numbers = [1, 2, 3, 4, 5]
numbers = [num ** 2 for num in numbers]
print(numbers)

# ) Use a dictionary comprehension to create a new dictionary from the dictionary below, where each of the values is title case.

movie = {
    "title": "thor: ragnarok",
    "director": "taika waititi",
    "producer": "kevin feige",
    "production_company": "marvel studios"
}

movie = {
    meta: info.title() for meta, info in movie.items()
}
print(movie)

# UNPACKING
# genrally used to perform several assignments at once

from os import major


movie = ("12 Angry Men", "Sidney Lumet", 1957)
# Rather than doing
# title = movie[0]
# director = movie[1]
# year = movie[2]
title, director, year = movie
print(title, director, year)
# What happened? Python recognizes we have 3 names we want to assign
# and the tuple has three elements. It assigns them in order 0, 1, 2
# Let's use it in a loop
movies = [
    (
        "Eternal Sunshine of the Spotless Mind",
        "Michel Gondry",
        2004
    ),
    (
        "Memento",
        "Christopher Nolan",
        2000
    ),
    (
        "Requiem for a Dream",
        "Darren Aronofsky",
        2000
    )
]
# Remember how we had to do a f string like
# for movie in movies:
#   print(f"{movie[0]} ({movie[2]}), by {movie[1]}")
for title, director, year in movies:
    print(f"{title} ({year}), by {director}")
# it works as above. Python sees there's a tuple with three elements, and that we want to assign three variable names, so it does so in order. It's important to note we can't do more or less than the elements in the tuple, otherwise we'll run into an error.

# An example of unpacking is ENUMERATION! A function called enumerate

names = ['Harry', 'Rachel', 'Brian']

for counter, name in enumerate(names):
    print(f"{counter}. {name}")
# enumerate will make a touple of (0, 'Harry'), (1, 'Rachel'), etc.
# but it will print =>
# 0. Harry
# 1. Rachel
# 2. Brian
# How do we get it to start at 1?
for counter, name in enumerate(names, start=1):
    print(f"{counter}. {name}")
# There we go.

for counter, movie in enumerate(movies, start=1):
    print(f"{counter}. {movie[0]}, ({movie[2]}), by {movie[1]}")
# would yield us (1, ("Eternal Sunshine..", "Michel Gondry", 2004))
# how can we make this better?

for counter, (title, director, year) in enumerate(movies, start=1):
    print(f"{counter}. {title} ({year}), by {director}")


# ZIP
# The zip function is an extremely powerful and versatile function used to combine two or more iterables into a single iterable.

pet_owners = ["Paul", "Andrea", "Marta"]
pets = ["Fluffy", "Bubbles", "Captain Catsworth"]
# zip will allow us to turn this into a new iterable which contains the following:

# ("Paul", "Fluffy"), ("Andrea", "Bubbles"), ("Marta", "Captain Catsworth")
# How do we use zip? To use it we call the function and pass the iterables we want to zip together.
pets_and_owners = zip(pet_owners, pets)
print(list(pets_and_owners))
# note we have to call list here because otherwise we'll get the object's location in memory.

# Using ZIP in loops!

for owner, pet in zip(pet_owners, pets):
    print(f"{owner} owns {pet}.")

# 1) Below is some simple data about characters from BoJack Horseman:

main_characters = [
    ("BoJack Horseman", "Will Arnett", "Horse"),
    ("Princess Carolyn", "Amy Sedaris", "Cat"),
    ("Diane Nguyen", "Alison Brie", "Human"),
    ("Mr. Peanutbutter", "Paul F. Tompkins", "Dog"),
    ("Todd Chavez", "Aaron Paul", "Human")
]
# The data contains the character name, the voice actor or actress who plays them, and the species of the character.

# Write a for loop that uses destructuring so that you can print each tuple in the following format:

# BoJack Horseman is a horse voiced by Will Arnet.
# Note that you're going to have to change the species information to lowercase when you print it. If you need a reminder on how to do this, we covered it in day 3 of the first week.

for character, voice, animal in main_characters:
    print(f"{character} is a {animal} voiced by {voice}")

# 2) Unpack the following tuple into 4 variables:

unpack_tuple = ("John Smith", 11743, ("Computer Science", "Mathematics"))
# The data represents a student's name, their student id number, and their major and minor disciplines in that order.
student_name, studient_id, (major, minor) = unpack_tuple
print(student_name, studient_id, major, minor)

# 3) Investigate what happens when you try to zip two iterables of different lengths. For example, try to zip a list containing three items, and a tuples containing four items.
letters = ['a', 'b', 'c']
numbers = (1, 2, 3, 4)
print(list(zip(letters, numbers)))
# [('a', 1), ('b', 2), ('c', 3)]
# zip stopped once it reached the end of letters
letters = ['a', 'b', 'c']
numbers = [1, 2]
print(list(zip(letters, numbers)))
# [('a', 1), ('b', 2)]
# now it stopped at the end of numbers?
# zip will stop once it reaches the end of the SHORTEST collection

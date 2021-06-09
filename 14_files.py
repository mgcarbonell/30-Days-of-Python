# Python can be used to minpulate files as well! It's amazing, isn't it?
# The first tool we need to work with files is the open function.
# We can pass a lot of arguments to open, but let's just start with one right now which is the file we want to access.

example_file = open('example.txt')
# Because example.txt is in the same directory as our main (14_files.py), we can just write the name of the file.
# We could have also done something like:
# example_file = open('./example.txt')
# Or even the full file path if we wanted to.

# So now that we've opened it, what do we do next? We can pass another function called read, which returns the opened document.
print(example_file.read())
# If we run 14_files we should see...
# ❯ python3 14_files.py
# Hello, from the example.txt file!
# Perfect, but we're missing something that's REALLY important.
# We need to close the file!
example_file.close()

# Another example of an argument that we can pass to open is read only access, we do this by passing the string "r"
example_file = open("example.txt", "r")
print(example_file.read())
example_file.close()

# We also have another way to access files, that's with 'write' mode, or 'w'
write_file = open("write_example.txt", "w")
write_file.close()
# If we do this we'll now have an empty file called write_example.txt
# Well, we can write directly to it!
write_file = open("write_example.txt", "w")
write_file.write("Welcome to the world, write_example.txt!")
write_file.close()

# What's another mode we can use? 'a' for append! We can append things to our file this way.

write_file = open("write_example.txt", "a")
write_file.write("\nNow you have two lines! You're growing up so fast!")
write_file.close()
# our write_example should now look something like this:
# Welcome to the world, write_example.txt!
# Now you have two lines! You're growing up so fast!

# Context managers:
# So far we've opened and closed files, and we have to do that each time. It's a little tediuos. However, Python gives us a little tool called a context manager, which handles these repetitive actions for us!

# This is what it looks like:
with open("example.txt", "r") as example_file:
    print(example_file.read())

# While this looks weird, it's functionally the same as the following:
# example_file = open("example.txt", "r")
# print(example_file.read())
# example_file.close()

# Let's break down the syntax:
# First we have 'with' which indicates to Python we're going to be using its context manager.
# Next we call 'open' just like before, but we're going to assign it to a variable
# We use 'as' to assign it to the variable example_file, and the rest is like normal!
# So all of the write_file = open, write_file.close() can be replaced with context, even the append. Check it out:

with open('write_example.txt', 'a') as write_file:
    write_file.write("\nNow you have three lines! You're going up so fast!")


# CSV data
# What is CSV? Comma separated values, it's the simplest way to store data as plain text. Usually this data is arranged like a table, where each row of values is on a different line of the file, all separated by commas.

# Let's create a new filed called iris.csv and put the data from https://www.teclado.com/30-days-of-python/python-30-day-14-files in there. It's a subset of the various famous data used used in machine learning called the "Iris flower data set"

# Our goal in this section: Take the set of CSV data, create a list of dictionaries from it.

# Step 1: Getting the data out of the file

# with open("iris.csv", "r") as iris_file:
#     iris_data = iris_file.read()

# Step 2: Splitting the data into rows
# We know something special about this document: the data is displayed on separate lines, meaning each line ends with a newline character to mark the line break. We can therefore split the data based on the "\n" character (newline)
# with open("iris.csv", "r") as iris_file:
#     iris_data = iris_file.read().split("\n")
# We COULD do this as above, but because this is a very common operation, Python gives us a tool to do the same thing. Instead of calling read, we'll call readlines.
# with open("iris.csv", "r") as iris_file:
    # iris_data = iris_file.readlines()
# The main difference is that readlines will preserve the "\n" character, however, so we'll need to remember to trim it out.

# Step 3 Creating our new list and trimming off the header row
# We create an empty list called irises, which is where our final dictionary will go.
# irises = []

# Now we iterate over the list in iris_data using a for loop. However, we need to remember that the first line isn't really data, it's just the table headers. So, we'll need to iterate over a slice.

# for row in iris_data[1:]:
#     pass

# Step 4: Splitting the rows into individual items
# For each iteration, we're going to strip off the new line character, and split the string using a comma as the delimiting string. So to make this easier, let's use split!

# for row in iris_data[1:]:
#     sepal_length, sepal_width, petal_length, petal_width, species = row.strip().split(',')

# Step 5: Creating a dictionary from each row.
with open("iris.csv", "r") as iris_file:
    iris_data = iris_file.readlines()

irises = []

for row in iris_data[1:]:
    sepal_length, sepal_width, petal_length, petal_width, species = row.strip().split(",")

    irises.append({
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width,
        "species": species
    })

# how cool is that? Well, there's even a different way! There's a dict function!
# Suppose we have the following list:
# iris = [
# 	("sepal_length", "5.1"),
# 	("sepal_width", "3.5"),
# 	("petal_length", "1.4"),
# 	("petal_width", "0.2"),
# 	("species", "Iris-setosa")
# ]
# If we pass the list to dict, Python will create this:
# {
# 	"sepal_length": "5.1",
# 	"sepal_width": "3.5",
# 	"petal_length": "1.4",
# 	"petal_width": "0.2",
# 	"species": "Iris-setosa"
# }
# We can mimic this as well with zip!

with open("iris.csv", "r") as iris_file:
    iris_data = iris_file.readlines()
# Rather than throwing away the header row, we'll store it and process it
headers = iris_data[0].strip().split(",")

irises = []

for row in iris_data[1:]:
    iris = row.strip().split(",")
    iris_dict = dict(zip(headers, iris))

    irises.append(iris_dict)

# NEATO!

# Exercises
# Rewrite the following piece of code using a context manager:

#  f = open("hello_world.txt", "w")
#  f.write("Hello, World!")
#  f.close()
# Use append mode to write "How are you?" on the second line of the hello_world.txt file above.
with open('hello_world.txt', 'w') as hello_world:
    hello_world.write("\nHello, World!")

# Take the list of dictionaries we created from the Iris flower data set and write it to a new file in CSV format.

# for iris in irises:
#     print (
#         f"{iris['sepal_length']}, {iris['sepal_width']}, {iris['petal_length']}," +
#         f"{iris['petal_width']},{iris['species']}"
#     )

with open('iris_2.csv', 'w') as iris_file:
    for iris in irises:
        iris_file.write(','.join(iris.values()) + '\n')

# Project
# Today is the end of the second week, so that means another end of week project!

# This time we're going to be creating a reading list application so that users can store information about books they want to read. This should help solidify the concepts we've been learning about over the past week.

# There are actually two versions of today's project, with different levels of difficulty.

# I'd recommend you have a go at the regular version first, because the harder version builds on the regular version, adding some more complex functionality.

# Good luck and happy coding!

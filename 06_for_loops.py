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

for movie in movies:
    print(f"{movie[0]} ({movie[2]}), by {movie[1]}")

# this is equal to

for m in movies:
    print(f"{m[0]}")

for movie_details in movies:
    print(f"{movie_details[0]}")

# next we have range

range(10)
# 0,1,2,3,4,5,6,7,8,9
# notice how range starts at the 0th index?
# so technically range(0, 10) would be the same as range(10)
# so we can define a START value such as 3
range(3, 10)
# 3,4,5,6,7,8,9
# we can also define a step value, increasing it by 2 each time
range(0, 10, 2)
# 0, 2, 4, 6, 8
range(0, 10, 3)
# 0, 3, 6, 9
# and we can reverse it
range(10, 0, -1)
# 10,9,8,7,6,5,4,3,2,1
# note that range(0, 10, -1) would give us an empty sequence.
# we can convert range to lists and tuples list(range(10)) gives us a list
# of 0 - 9.
# tuple(range(10)) gives us a tuple of 0-9
# we can iterate through range with a for loop
# Want to print "Hello" ten times?
for _ in range(10):
    print("Hello!")
# why the _? _ is the variable name, we're not using something like a number or
# returning the value. However where we wouldn't want to do this is making a
# loop like for _ in range(10): why? Because we don't want to return blanks,
# we'd usually want to return a number.

# 1) Below we've provided a list of tuples, where each tuple contains details
# about an employee of a shop: their name, the number of hours worked last
# week, and their hourly rate. Print how much each employee is due to be paid
# at the end of the week in a nice, readable format.

employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]
for employee in employees:
    weekly = employee[1] * employee[2]
    print(
        f"{employee[0]} weekly paycheck is: ${weekly}.")

# 2) For the employees above, print out those who are earning an hourly wage
# above average.

total = 0
count = 0
for employee in employees:
    total = total + employee[2]
    count = count + 1

average = total / count
for employee in employees:
    if employee[2] > average:
        print(f"{employee[0]} is paid more than the average.")

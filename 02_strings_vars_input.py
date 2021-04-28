# exercises:
# Ask the user for their name and age, assign these values to two variables and print them out.
name = input("What is your name? ")
age = int(input("And what is your age? "))
print(f"Hello {name}, you are {age} years old.")

# Investigate what happens when you try to assign a value to a variable that you've already defined. Try printing the variable before and after you reuse name.

print(name)
name = 'Wario'
print(name)

# Below you will find some code with a number of errors: Try to go through the program line by line and fix the issues in the code. I'd encourage you to try running the program while you're working on it, as reading the error messages is great practice for debugging your own programs.

# hourly_wage = input("Please enter your hourly wage: ')
hourly_wage = input('Please enter your hourly wage: ')

# prnt("Hourly wage: ")
print('Hourly wage: ')

# print(hourlywage)
print(hourly_wage)

# print("Hours worked: ")
# print(hours_worked)

hours_worked = input("How many hours did you work this week? ")
print("hours worked: ")
print(hours_worked)

# For loops are great for two kinds of repeated actions:
# 1. When we want to do something for each item in some group.
# 2. When we want to do something a set number of times.
# What if we want to perform an action as many times as needed until some
# condition is met?
# What if we want to perform the same action forever? Well there's an app
# for that, just kidding it's called a while loop.

user_number = input("Please enter a number: ")

while int(user_number) < 10:
    print("Your number was less than 10.")
    user_number = input("Please select another number: ")

print("Your number was at least 10.")

# We can also purposefully specify infinite loops. Why might we want an infinite
# loop? Well remember that hangman game that ran all the desginated functions
# WHILE the game state was TRUE? while True: is a valid infinite loop.

# So let's check this out:
while True:
    selected_option = input(
        "Please enter 'a', 'b', or 'c', or enter 'q' to quit: ")

    if selected_option == "a":
        print("You selected option 'a'!")
    elif selected_option == "b":
        print("You selected option 'b'!")
    elif selected_option == "c":
        print("You selected option 'c'!")
    elif selected_option == "q":
        print("You selected option 'q'! Quitting the menu!")
        break
    else:
        print("You selected an invalid option.")

# we sometimes might notice someone saying `while 1:` this is because 1 is a
# truthy value.

# As we know we can use `break`, we can also use `continue`
# ex: print even numbers
for number in range(10):
    if number % 2 != 0:
        continue
    print(number)

# We also have an ELSE clause with loops that are a little different than the
# else clause in if/else.

# "it's worth thinking about else as a "no break" clause when we use it with
# loops." What do we mean by a 'no break' clause?

# "The reason I say it's good to think about else as meaning "no break", is because an else clause attached to a loop will only run if a break statement wasn't encountered during the execution of that loop."

# Let's look at an example:

# Get a number to test from the user
dividend = int(input("Please enter a number: "))

# Grab numbers one at a time from the range sequence
for divisor in range(2, dividend):
    # If user's number is divisible by the curent divisor, break the loop
    if dividend % divisor == 0:
        print(f"{dividend} is not prime!")
        break
else:
    # This line only runs if no divisors produced integer results
    print(f"{dividend} is prime!")

# We can do the same with a WHILE loop

# Get a number to test from the user, and set the initial divisor to 2
dividend = int(input("Please enter a number: "))
divisor = 2

# Keep looping until the divisor equals the number we're testing
while divisor < dividend:
    # If user's number is divisible by the curent divisor, break the loop
    if dividend % divisor == 0:
        print(f"{dividend} is not prime!")
        break

    # Increment the divisor for the next iteration
    divisor = divisor + 1
else:
    # This line only runs if no divisors produced integer results
    print(f"{dividend} is prime!")


# Exercises

# 1) Write a short guessing game program using a while loop. The user should be prompted to guess a number between 1 and 100, and you should tell them whether their guess was too high or too low after each guess. The loop should keeping running until the user guesses the number correctly.

user_guess = int(input("Please guess a number between 1 and 100: "))
magic_number = 46

while True:
    if user_guess < magic_number:
        user_guess = int(input("Your guess was too low! Guess again: "))
    elif user_guess > magic_number:
        user_guess = int(input("Too high! Guess again: "))
    elif user_guess == magic_number:
        print("Congratulations! That's the magic number!")
        break


# 2) Use a loop and the continue keyword to print out every character in the string "Python", except the "o".
# Remember that strings are collections, and they are iterable, so you can iterate over the string, which will yield one character at a time.

# string = "Python"
word = "Python"
for char in word:
    if char == 'o':
        continue
    print(char)


# 3) Using one of the examples from earlier—or a solution entirely of your own—create a program that prints out every prime number between 1 and 100.

primes = []

for x in range(2, 101):
    for y in range(2, x):
        if x % y == 0:
            break
    else:
        primes.append(x)

print(primes)

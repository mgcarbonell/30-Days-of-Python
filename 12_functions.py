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

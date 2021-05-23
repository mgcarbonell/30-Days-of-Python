# PROJECT BRIEF
# The program you write for this project should do the following:

# 1) It should be able to accept a card number from the user. For this project, you can assume that the number will be entered as a single string of characters (i.e. there won't be any spaces between the numbers). However, you should be able to accept a card number with spaces at the start or end of the string.

# If you want to challenge yourself, you should try to be more versatile with regards to the format that you accept card numbers in.

# You may want to turn the user's input into a list of numbers, as that will make it easier to work with.

# 2) The program should validate that card number using the Luhn algorithm described above. You should implement this algorithm yourself.

# After removing the checking digit and reversing the card number, you'll need a for loop to go over the credit card numbers. As you go through each digit, you must find a way to determine whether a digit is in an odd or an even position. Remember you can check the model solution if you get stuck!

# 3) Once the validation is complete, the program should inform the user whether or not the card number is valid by printing a string to the console.

# This program must pass the Luhn algorithm.

# 1. Remove the rightmost digit from the card number. This number is called the
#    checking digit, and it will be excluded from most of our calculations.
# 2. Reverse the order of the remaining digits.
# 3. For this sequence of reversed digits, take the digits at each of the even
#    indices(0, 2, 4, 6, etc.) and double them. If any of the results are
#    greater than 9, subtract 9 from those numbers.
# 4. Add together all of the results and add the checking digit.
# 5. If the result is divisible by 10, the number is a valid card number. If
#    it's not, the card number is not valid.

#  _______________________________________________________
# | NUMBER                | OPERATION                     |
# |-----------------------|-------------------------------|
# | 5893804115457289      | Start number                  |
# | 589380411545728X      | Remove the last digit         |
# | 827545114083985X      | Reverse the remaining digits  |
# | 16214585218016318810X | Double digits at even indices |
# | 725585218073981X      | Subtract 9 if over 9          |
# '-----------------------'-------------------------------'
# 7 + 2 + 5 + 5 + 8 + 5 + 2 + 1 + 8 + 0 + 7 + 3 + 9 + 8 + 1 + 9
# We get 80. 80 is divisible by 10, the number is valid.

card_number = list(input("Please enter a number to validate: ").strip())
# remove check digit
check_digit = card_number.pop()
# reverse the remaining digits
card_number.reverse()
# double digits at even dicies

processed_digits = []

for index, number in enumerate(card_number):
    if index % 2 == 0:
        doubled_digit = int(number) * 2
        if doubled_digit > 9:
            doubled_digit = doubled_digit - 9

        processed_digits.append(doubled_digit)
    else:
        processed_digits.append(int(number))

total = int(check_digit) + sum(processed_digits)
if total % 10 == 0:
    print("Valid")
else:
    print("Invalid")

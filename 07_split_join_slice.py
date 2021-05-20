numbers = [1, 2, 3, 4, 5]
numbers = str(numbers)
# we get [1, 2, 3, 4, 5] (except they're strings)
# if we pass to print we may notice we get the same
# that's because print converts the list to a string.
# "[1, 2, 3, 4, 5]"
# What if we want just 1, 2, 3, 4, 5?
# What if I want...
# The people who worked on this project are: Mike, Sofia, Helen.
# What we don't want is something dumb like...
# ...are: [Mike, Sofia, Helen].
# How did we get to the above? With join()

project_authors = ["Mike", "Sofia", "Helen"]
project_authors = ", ".join(project_authors)
print(f"The people who worked on this project are: {project_authors}.")

# we can also call this in a different, inline, manner:
project_authors = ["Mike", "Sofia", "Helen"]
print(
    f"The people who worked on this project are: {', '.join(project_authors)}")
# same output!
# Be aware: join can only be performed on strings. If we want to join nums we
# have to convert.
numbers = [1, 2, 3, 4, 5]

stringified_numbers = []

for number in numbers:
    stringified_numbers.append(str(number))

print(', '.join(stringified_numbers))
# 1, 2, 3, 4, 5

# okay so we've joined them, but what about taking them apart?
# here comes the more common method: split!
# user_numbers = input("Please enter 5 numbers sperated by commas. ")
# 1,2,3,4,5
# we can convert to an array with split (by default)
# numbers_list = user_numbers.split(',')  # splits it on the comma.
# print(numbers_list)  # ['1', '2', '3', '4', '5']

# what if I wanted a list of tuples?
# user_numbers = input("Please enter 5 numbers sperated by dashes. ")
# 1-2-3-4-5
# numbers_tuple = tuple(user_numbers.split('-'))
# print(numbers_tuple)  # ('1', '2', '3', '4', '5')

# Be cautious though! Split won't strip white space, so if a user enters
# something like 1, 2, 3, 4, 5 or 1 - 2 - 3 - 4 - 5 we would end up getting
# ['1', ' 2', ' 3', ' 4', ' 5'] or ('1', ' 2 ', ' 3 '...)
# while this isn't usually an issue, if we do need to account for that that
# we would need to use a for loop and strip.
# user_numbers = input("Please enter 5 nubmers separated by commas: ")
# 1, 2, 3, 4, 5
# user_numbers = user_numbers.split(',')

# numbers_list = []

# for number in user_numbers:
# numbers_list.append(number.strip())
#
# print(numbers_list)

# What if I just want a part of a string? Not the entire thing?
# Well, let's check out slicing.
original_string = "Python"
sliced_string = original_string[0:3]
# Pyt
print(sliced_string)
# What's going on with [0:3]? It's an instruction to the slice:
# start at index 0
# go up to, but not including index 3
# from 0 up to 3 [0:3] but we could've also just used [:3]
# and if we had wrote it as [3:] we'd get hon, because it starts at index 0 and
# goes to the end of the string.
# We can also go backwards! [3:-1] would chop off the n and return ho
# we can also take a copy using [:]


# Exercises
# 1) Ask the user to enter their given name and surname in response to a single prompt. Use split to extract the names, and then assign each name to a different variable. For this exercise, you can assume that the user has a single given name and a single surname.

user_input = input("Please enter your given name and surname. ")
sliced_name = user_input.split()
first_name = sliced_name[0]
surname = sliced_name[1]
print(f"Hello {first_name} {surname}")


# 2) Print the list, [1, 2, 3, 4, 5], in the format 1 | 2 | 3 | 4 | 5 using the join method. Remember that you can only join collections of strings, so you’re going to need to do some initial processing of the list of numbers.

numbers = [1, 2, 3, 4, 5]

string_numbers = []

for number in numbers:
    string_numbers.append(str(number))

print(' | '.join(string_numbers))


# 3) Below you’ll find a short list of quotes:

quotes = [
    "'What a waste my life would be without all the beautiful mistakes I've made.'",
    "'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
    "'The very essence of romance is uncertainty.'",
    "'We are not here to do what has already been done.'"
]

# Each quote is a string, but each string actually contains quote characters at the start and end. Using slicing, extract the text from each string, without these extra quote marks, and print each quote.
# first_quote = quotes[0]
# print(first_quote[1:-1])
# second_quote = quotes[1]
# print(second_quote[1:-1])
# third_quote = quotes[2]
# print(third_quote[1:-1])
for quote in quotes:
    print(quote[1:-1])

# You may also want to try a solution using strip.

# 4) Ask the user to enter a word, and then print out the length of the word. You should account for any excess whitespace in the user’s input, so you’re going to have to process the string before you find its length.
user_word = input("Please enter a word to find it's length: ").strip()
char_count = len(user_word)
print(f"The length of the word is: {char_count}")

# If you want to take this a little bit further, you an ask the user for a long piece of text. You can then tell them how many how many characters are in the text overall, and you can also provide them a word count.
user_text = input("Please enter a few words to find their length: ").strip()
char_text = len(user_text)
word_text = len(user_text.split())
print(
    f"The sample text contains \n Characters: {char_text} \n Words: {word_text}")

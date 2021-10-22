# IMPORTS RECAP
# Importing adds a name to globals()
# Importing allows use to access elements of the imported module
# import math
# print (math.pi) # 3.14
# We can also use * to add almost everything from a module to your global 
# namespace. Though, this can "pollute" our global namespace. Not exactly 
# encouraged.

# WORKING WITH TWO FILES
# import myfile

# What happens when we import a file? Python RUNS the file!
print("What's going on?")
# => "Hello, world!"
# => "WHat's going on?"

# try:
#   myfile.get_user_age()
# except ValueError:
#   print("That's not a valid value for your age!")

# So in a sense it's like JS. Use dot notation <imported file>.<thing we want>
# That's the gist of it: separate things into files and import them!
# Don't give your files the same names as built-in modules.
# Don't create a new file and call it json.py and try to import it because 
# you'll be dealing with your file and not all the other things that come from 
# the python built in json lib.

# YOUR FILES WORK THE SAME WAS AS MODULES

# Everything we could do with external modules, we can dowith our own files!
# importing the whole file import myfile and then referring to things myfile.x
# Importing specific things with from myfile import x
# Aliased imports
# We could even do from myfile import * (although that's discouraged)

# Can we do this with files and folders? Yup, sure can.
# For example, create a folder in your project called user_interactions and move myfile.py into it. Now your file/folder structure will look like this:

# - main.py
# - user_interactions/
#     | - myfile.py
# From main.py you now have to use slightly different syntax to import myfile.py:

from user_interactions.myfile import get_user_age

try:
  get_user_age()
except ValueError:
  print("That's not a valid value for your age! Whole numbers!")

# when importing the . means 'look inside'
# so in our import statement we're saying: Look for myfile inside 
# user_interactions.

# If we have multiple sub folders?
# from folder.subfolder.module import something_from_the_module

# SCRIPT MODE VERSUS MODULE MODE

# When we run a file we say that file is ran in "script mode"
# When we import a file, that file runs in "module mode"
# If we were to do the following:
# put in myfile.py: print(__name__)
# And in main.py:
# import user_interactions.myfile
# print(__name__)
# our output when we run main.py would be:
# user_interactions.myfile
# __main__

# Remember that when we import, we run the file. Therefore the first line of 
# output belongs to myfile.py, and the second line of output belongs to main.py.

# The file that we run always has a __name__ variable with a value of 
# "__main__". That is simply how Python tells us that we ran that file.

# Any file that doesn't have a __name__ equal to "__main__" was imported.

# RUNNING CODE ONLY IN SCRIPT MODE
# We could type this in myfile.py:

# def get_user_age():
#     return int(input("Enter your age: "))

# if __name__ == "__main__":
#     get_user_age()

# EXERCISES
# 1. Split the book reader into multiple files and import
import database


USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit
Your choice: """
BOOKS_FILE = 'books.json'


def menu():
    database.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()

        user_input = input(USER_CHOICE)

def prompt_add_book():
    name = input('Enter the new book name: ')
    author = input('Enter the new book author: ')

    database.insert_book(name, author)


def list_books():
    for book in database.get_all_books():
        read = 'YES' if book['read'] == '1' else 'NO'  # book[3] will be a falsy value (0) if not read
        print(f"{book['name']} by {book['author']} — Read: {read}")


def prompt_read_book():
    name = input('Enter the name of the book you just finished reading: ')

    database.mark_book_as_read(name)



def prompt_delete_book():
    name = input('Enter the name of the book you wish to delete: ')

    database.delete_book(name)





menu()

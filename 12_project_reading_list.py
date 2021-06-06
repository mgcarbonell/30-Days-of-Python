# Users should be able to add a book to their reading list by providing a book title, an author's name, and a year of publication.
# The program should store information about all of these books in a Python list.
# Users should be able to display all the books in their reading list, and these books should be printed out in a user-friendly format.
# Users should be able to select these options from a text menu, and they should be able to perform multiple operations without restarting the program. You can see an example of a working menu in the post on while loops(day 8).

# a reading list
# add to a reading list
# enter/add information about the books
# 'should store information about all these books in a python list'
# list containing dictionaries or tuples.
# If we had a tuple it would just be ("Title", year, "Author")
# If we had a dictionary { 'title': 'text', 'year': int, 'author': 'text'}
# display all books printed out nicely
# "Title" (publishing year) by Author
# perform multiple operations without restarting while True, on = True, etc.


# store the books
book_list = []

menu = """ Hello,

Please select from one of the following options:

> a ... To add a book to your list.
> l ... To list all of yours books.
> q ... To quit.

"""
# strip the white space, make it all lower case
selected_option = input(menu).strip().lower()


def add_book():
    print("Adding...")
    title = input("Title: ").strip().title()
    author = input("Author: ").strip().title()
    year = input("Year of publication: ").strip()

    new_entry = {
        "title": title,
        "author": author,
        "year": year
    }

    book_list.append(new_entry)


def show_books():
    for book in book_list:
        title, author, year = book.values()
        print(f"{title}, by {author} ({year})\n")


while selected_option != 'q':
    if selected_option == 'a':
        add_book()
    elif selected_option == 'l':
        show_books()
    else:
        print(f"Sorry,'{selected_option}' is not a valid option.")

    selected_option = input(menu).strip().lower()

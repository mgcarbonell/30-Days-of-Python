# Users should be able to add a book to their reading list by providing a book
# title, an author's name, and a year of publication.

# The program should store information about all of these books in a file
# called books.csv, and this data should be stored in CSV format.

# Users should be able to retrieve the books in their reading list, and these
# books should be printed out in a user-friendly format.

# Users should be able to search for a specific book by providing a book title.

# Users should be able to select these options from a text menu, and they
# should be able to perform multiple operations without restarting the program.
# You can see an example of a working menu in the post on while loops(day 8).

# book_list = []

menu = """ Hello,

Please select from one of the following options:

> a ... To ADD a book to your list.
> d ... To DELETE a book from your list.
> l ... To LIST all of yours books.
> r ... To mark a book as READ.
> s ... To SEARCH for a book.
> q ... To QUIT.

> ... """
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


def show_books(books):
    print()
    for book in book_list:
        title, author, year = book.values()
        print(f"{title}, by {author} ({year}) - {book['read']}\n")


def get_all_books():
    books = []

    with open('books.csv', 'r') as book_list:
        for book in book_list:
            title, author, year, read_status = book.strip().split(',')

            books.append({
                "title": title,
                "author": author,
                "year": year,
                "read": read_status
            })

    return books


def delete_book(books, book_to_delete):
    books.remove(book_to_delete)


def find_book():
    book_list = get_all_books()
    matching_books = []

    search_term = input("Please enter a book title: ").strip().lower()

    for book in book_list:
        if search_term in book["title"].lower():
            matching_books.append(book)

    return matching_books


def mark_book_as_read(books, book_to_update):
    index = books.index(book_to_update)
    books[index]['read'] = 'Read'


def update_reading_list(operation):
    books = get_all_books()
    matching_books = find_books()

    if matching_books:
        operation(books, matching_books[0])

        with open('books.csv', 'w') as reading_list:
            for book in books:
                reading_list.write(
                    f"{book['title']},{book['author']},{book['year']},{book['read']}\n")

    else:
        print("Apologies, no matching titles found.")


while selected_option != 'q':
    if selected_option == 'a':
        add_book()
    elif selected_option == 'l':
        # Retrieve the whole reading list for printing
        reading_list = get_all_books()

        # check if reading_list contains at least one book
        if reading_list:
            show_books(reading_list)
        else:
            print("Apologies, your reading list is empty.")
    elif selected_option == 'd':
        update_reading_list(delete_book)
    elif selected_option == 'r':
        update_reading_list(mark_book_as_read)
    elif selected_option == 's':
        matching_books = find_book()

        if matching_books:
            show_books(matching_books)

        else:
            print("Apologies, we did not find any books for that search term.")

    else:
        print(f"Sorry,'{selected_option}' is not a valid option.")

    selected_option = input(menu).strip().lower()

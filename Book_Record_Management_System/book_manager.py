import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "books.json"


def load_books():
    """Read book records from the JSON file."""
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read the data file. Starting with an empty list.")
        return []


def save_books(books):
    """Save all book records to the JSON file."""
    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(books, file, indent=4)
        print("Records saved successfully.")
    except OSError:
        print("Error: Unable to save the records.")


def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty. Please try again.")


def get_positive_integer(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number > 0:
                return number
            print("Please enter a number greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def find_book_index(books, book_id):
    for index, book in enumerate(books):
        if book["book_id"] == book_id:
            return index
    return -1


def add_book(books):
    print("\n--- Add a New Book ---")
    book_id = get_non_empty("Enter book ID: ")

    if find_book_index(books, book_id) != -1:
        print("A book with this ID already exists.")
        return

    title = get_non_empty("Enter book title: ")
    author = get_non_empty("Enter author name: ")
    quantity = get_positive_integer("Enter quantity: ")

    # Each book is stored as a dictionary; all dictionaries are kept in a list.
    book = {
        "book_id": book_id,
        "title": title,
        "author": author,
        "quantity": quantity
    }
    books.append(book)
    save_books(books)
    print("Book added successfully.")


def display_books(books):
    print("\n--- All Book Records ---")
    if not books:
        print("No book records found.")
        return

    # Tuple used to keep the table headings together.
    headings = ("Book ID", "Title", "Author", "Quantity")
    print("-" * 75)
    print(f"{headings[0]:<12} {headings[1]:<25} {headings[2]:<22} {headings[3]:>8}")
    print("-" * 75)

    for book in books:
        print(
            f"{book['book_id']:<12} "
            f"{book['title'][:24]:<25} "
            f"{book['author'][:21]:<22} "
            f"{book['quantity']:>8}"
        )
    print("-" * 75)


def search_book(books):
    print("\n--- Search for a Book ---")
    keyword = get_non_empty("Enter book ID or title: ").lower()

    matches = [
        book for book in books
        if keyword == book["book_id"].lower()
        or keyword in book["title"].lower()
    ]

    if not matches:
        print("No matching book was found.")
        return

    for book in matches:
        print(
            f"ID: {book['book_id']} | Title: {book['title']} | "
            f"Author: {book['author']} | Quantity: {book['quantity']}"
        )


def update_book(books):
    print("\n--- Update Book Details ---")
    book_id = get_non_empty("Enter the book ID to update: ")
    index = find_book_index(books, book_id)

    if index == -1:
        print("Book not found.")
        return

    book = books[index]
    print("Press Enter to keep the existing value.")
    new_title = input(f"Title [{book['title']}]: ").strip()
    new_author = input(f"Author [{book['author']}]: ").strip()
    new_quantity = input(f"Quantity [{book['quantity']}]: ").strip()

    if new_title:
        book["title"] = new_title
    if new_author:
        book["author"] = new_author
    if new_quantity:
        try:
            quantity = int(new_quantity)
            if quantity <= 0:
                print("Quantity must be greater than zero. Keeping old quantity.")
            else:
                book["quantity"] = quantity
        except ValueError:
            print("Invalid quantity. Keeping old quantity.")

    save_books(books)
    print("Book details updated.")


def delete_book(books):
    print("\n--- Delete a Book ---")
    book_id = get_non_empty("Enter the book ID to delete: ")
    index = find_book_index(books, book_id)

    if index == -1:
        print("Book not found.")
        return

    removed_book = books.pop(index)
    save_books(books)
    print(f"'{removed_book['title']}' has been deleted.")

from book_manager import (
    add_book, display_books, search_book, update_book,
    delete_book, load_books
)


def show_menu():
    print("\n========== BOOK RECORD MANAGEMENT SYSTEM ==========")
    print("1. Add a book")
    print("2. Display all books")
    print("3. Search for a book")
    print("4. Update a book")
    print("5. Delete a book")
    print("6. Exit")
    print("===================================================")


def main():
    # Loading the saved records when the program starts
    books = load_books()

    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_book(books)
        elif choice == "2":
            display_books(books)
        elif choice == "3":
            search_book(books)
        elif choice == "4":
            update_book(books)
        elif choice == "5":
            delete_book(books)
        elif choice == "6":
            print("Thank you for using the Book Record Management System!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()

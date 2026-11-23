# Book Record Management System

## Project Information
**Problem Statement:** 6 - Simple inventory or book-record management application using compound data structures and files.

**Language:** Python 3

## Introduction
The Book Record Management System is a simple, menu-driven Python application. It helps a user maintain book details such as book ID, title, author, and quantity. The records are saved in a JSON file, so they remain available after the program is closed.

## Objectives
- To store and manage book details.
- To practise lists, tuples, and dictionaries.
- To use file handling for permanent storage.
- To apply functions, input validation, and exception handling.

## Features
1. Add a new book.
2. Display all books.
3. Search by book ID or title.
4. Update an existing book.
5. Delete a book.
6. Save records automatically in `books.json`.

## Project Structure
```text
Book_Record_Management_System/
|-- main.py
|-- book_manager.py
|-- books.json
|-- README.md
|-- requirements.txt
```

## Concepts Used
- **List:** Stores all book records.
- **Dictionary:** Stores the details of one book.
- **Tuple:** Stores the table headings.
- **Functions:** Divides the program into reusable tasks.
- **File handling:** Reads and writes records in `books.json`.
- **Exception handling:** Handles invalid numbers and file errors.
- **Validation:** Checks empty fields, duplicate IDs, and positive quantities.

## Requirements
- Python 3.8 or later
- No external libraries are required.

## How to Run
1. Download or clone this project.
2. Open the project folder in VS Code or a terminal.
3. Run:

```bash
python main.py
```

4. Select an option from the menu and follow the instructions.

## Sample Output
```text
========== BOOK RECORD MANAGEMENT SYSTEM ==========
1. Add a book
2. Display all books
3. Search for a book
4. Update a book
5. Delete a book
6. Exit
===================================================
Enter your choice (1-6): 1

--- Add a New Book ---
Enter book ID: B101
Enter book title: Python Basics
Enter author name: R. Sharma
Enter quantity: 5
Records saved successfully.
Book added successfully.
```

## Data Storage
Book details are stored in `books.json`. The application loads this file when it starts and updates it whenever a record is added, changed, or deleted.

## Conclusion
This project demonstrates how Python data structures and file handling can be used to create a useful record-management application. It provides basic operations in a simple and user-friendly menu.

## GitHub Upload Instructions
1. Sign in to [GitHub](https://github.com/).
2. Click **New repository**.
3. Enter the repository name: `Book-Record-Management-System`.
4. Select **Public** (if your teacher requires a public repository).
5. Click **Create repository**.
6. Choose **Add file → Upload files**.
7. Upload `main.py`, `book_manager.py`, `books.json`, `README.md`, and `requirements.txt`.
8. Click **Commit changes**.

### Optional: Upload using Git
Run these commands inside the project folder after creating an empty GitHub repository:

```bash
git init
git add .
git commit -m "Add Book Record Management System"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/Book-Record-Management-System.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username.

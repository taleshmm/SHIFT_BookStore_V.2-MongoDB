# Python Bookstore Project (Version 2.0) - PostgreSQL

Welcome to the Python Bookstore Project! This project has been updated to incorporate a PostgreSQL database for data storage and retrieval. It's a bookstore application developed using object-oriented principles, conditional structures, loops, functions, and lists.

In this version, data is stored in an existing PostgreSQL database, and the application includes additional features for reading data from CSV or JSON files, exporting data to these formats, and inserting multiple records at once.

## Main Features

1. **Add Book:** Allows you to add new books to the bookstore. Each book will have a title, author, publication year, and other relevant information.

2. **Search Book:** Enables you to search for books in the bookstore based on different attributes, such as title, author, publication year, etc.

3. **Delete Book:** Permits the removal of books from the bookstore based on a unique identifier.

4. **Search by Specific Attribute:** Allows searching for books based on a specific attribute, such as all books by a particular author.

5. **Read, Export, and Insert Data:** The application now supports reading data from CSV or JSON files, exporting data to these formats, and inserting multiple records from these files into the existing PostgreSQL database.

## How to Use

1. Make sure you have Python installed on your system.

2. Clone this repository to your computer.

3. **Database Setup:** Before using the application, make sure you have access to an existing PostgreSQL database. You'll need to configure the connection details in the application code. Look for the database configuration section in the code and provide the necessary information.

4. **Important Note**: To use the file reading functions, move the files from the "others" folder located in the test files directory to the project's root directory.

5. Execute the `main.py` file using the following command:

6. Follow the terminal prompts to interact with the application. Use the numeric options to select the desired action.

## Project Structure

The project is organized as follows:

- `dao/`: Contains files related to data access objects for PostgreSQL.
- `model/`: Contains class definitions that represent project objects.
- `service/`: Contains the application's business logic.
- `utils/`: Contains utility functions and shared resources.
- `others/`: Contains sample CSV and JSON files for testing and data import.

## Next steps

This release represents a significant update to the Python Bookstore Project, with PostgreSQL integration and improved data management features. In the next steps I will implement a front-end for better use of the system:

Thanks! Please feel free to contribute, report issues or suggest improvements.

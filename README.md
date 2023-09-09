# Python Bookstore Project (Version 2.0) - MongoDB

Welcome to the Python Bookstore Project! This project has been updated to incorporate MongoDB for data storage and retrieval. It's a bookstore application developed using object-oriented principles, conditional structures, loops, functions, and lists.

In this version, data is stored in MongoDB, and the application includes additional features for reading data from CSV or JSON files, exporting data to these formats with category, author, and editor names, and inserting multiple records at once.

## Main Features

1. **Add Book:** Allows you to add new books to the bookstore. Each book will have a title, author, publication year, and other relevant information.

2. **Search Book:** Enables you to search for books in the bookstore based on different attributes, such as title, author, publication year, etc.

3. **Delete Book:** Permits the removal of books from the bookstore based on a unique identifier.

4. **Search by Specific Attribute:** Allows searching for books based on a specific attribute, such as all books by a particular author.

5. **Read, Export, and Insert Data:** The application now supports reading data from CSV or JSON files, exporting data to these formats with category, author, and editor names, and inserting multiple records from these files into MongoDB.

## How to Use

1. Make sure you have Python installed on your system.

2. Clone this repository to your computer.

3. **MongoDB Setup:** Before using the application, ensure you have MongoDB installed and running locally or on a server. Configure the MongoDB connection details in the application code. Look for the database configuration section in the code and provide the necessary information.

4. **Important Note**: To use the file reading functions, move the files from the "others" folder located in the test files directory to the project's root directory.

5. Execute the `main.py` file using the following command:

6. Follow the terminal prompts to interact with the application. Use the numeric options to select the desired action.

## Project Structure

The project is organized as follows:

- `dao/`: Contains files related to data access objects for MongoDB.
- `model/`: Contains class definitions that represent project objects.
- `service/`: Contains the application's business logic.
- `utils/`: Contains utility functions and shared resources.
- `others/`: Contains sample CSV and JSON files for testing and data import.

## Next Steps

This release represents a significant update to the Python Bookstore Project, with MongoDB integration and improved data export functionality. In the next steps, you may consider the following improvements:

- Implement a user-friendly front-end interface for better usability.
- Enhance security features, such as authentication and authorization.
- Prepare the application for deployment on a cloud platform or server.

Thanks! Please feel free to contribute, report issues, or suggest improvements.

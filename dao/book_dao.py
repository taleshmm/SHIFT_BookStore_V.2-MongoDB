from model.book import Book
from database.connection_factory import ConnectionFactory

class BookDAO:
    def __init__(self):
        self.__connection_factory = ConnectionFactory()
    
    def getAll(self) -> list[Book]:
        connect = self.__connection_factory.get_connection()
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM books")
        rows = cursor.fetchall()
        cursor.close()
        connect.close()
        books = list()
        for row in rows:
            bookRow = Book(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[0])
            books.append(bookRow)
        return books
    
    def create(self, book: Book) -> None:
        connect = self.__connection_factory.get_connection()
        cursor = connect.cursor()
        cursor.execute("INSERT INTO books (title, isbn, pages, yearBook, summary, category_id, publisher_id, author_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (book.title, book.isbn, book.pages, book.year, book.summary, book.category, book.editor, book.author))
        connect.commit()
        cursor.close()
        connect.close()

    def delete(self, id: int) -> bool:
        connect = self.__connection_factory.get_connection()
        cursor = connect.cursor()
        cursor.execute("DELETE FROM books WHERE id = %s", (id,))
        rows_deleted = cursor.rowcount
        connect.commit()
        cursor.close()
        connect.close()
        if rows_deleted > 0:
            return True
        return False
    
    def getById(self, id: int) -> Book:
        connect = self.__connection_factory.get_connection()
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM books WHERE id = %s", (id,))
        row = cursor.fetchone()
        cursor.close()
        connect.close()
        book_found = None
        if row:
            book_found = Book(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[0])
        return book_found
    
    def getByTitle(self, title: str) -> Book:
       connect = self.__connection_factory.get_connection()
       cursor = connect.cursor()
       cursor.execute("SELECT * FROM books   WHERE title = %s", (title,))
       row = cursor.fetchone()
       cursor.close()
       connect.close()
       book_found = None
       if row:
           book_found = Book(row[1], row   [2], row[3], row[4], row[5], row [6], row[7], row[8], row[0])
       return book_found
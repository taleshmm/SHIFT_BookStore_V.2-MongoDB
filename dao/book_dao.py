from model.book import Book
from database.client_factory import ClientFactory
from bson import ObjectId
class BookDAO:
    def __init__(self):
        self.__client_factory = ClientFactory()
    
    def getAll(self) -> list[Book]:
        books = list()
        client = self.__client_factory.get_client()
        db = client.bookStore
        for doc in db.books.find():
            aut = Book(doc.get('title', 'No data'), doc.get('isbn', 'No data'), doc.get('pages', 'No data'), doc.get('year', 'No data'), doc.get('summary', 'No data'), doc.get('category', 'No data'), doc.get('publisher', 'No data'), doc.get('author', 'No data'))
            aut.id = doc['_id']
            books.append(aut)
        client.close()
        return books
    
    def create(self, book: Book) -> None:
        client = self.__client_factory.get_client()
        db = client.bookStore
        db.books.insert_one({'title': book.title, 'isbn': book.isbn, 'pages': book.pages, 'year': book.year, 'summary': book.summary, 'category': book.category, 'publisher': book.publisher, 'author': book.author})
        client.close()

    def delete(self, id: int) -> bool:
        client = self.__client_factory.get_client()
        db = client.bookStore
        result = db.books.delete_one({'_id': ObjectId(id)})
        client.close()
        if result.deleted_count == 1:
            return True
        return False
    
    def getById(self, id: int) -> Book:
        client = self.__client_factory.get_client()
        db = client.bookStore
        result = db.books.find_one({'_id': ObjectId(id)})
        client.close()
        book_found = None
        if result:
            book_found = Book(result.get('title', 'No data'), result.get('isbn', 'No data'), result.get('pages', 'No data'), result.get('year', 'No data'), result.get('summary', 'No data'), result.get('category', 'No data'), result.get('publisher', 'No data'), result.get('author', 'No data'))
        return book_found
    
    def getByTitle(self, title: str) -> Book:
        client = self.__client_factory.get_client()
        db = client.bookStore
        result = db.books.find_one({'title': title})
        client.close()
        book_found = None
        if result:
            book_found = Book(result.get('title', 'No data'), result.get('isbn', 'No data'), result.get('pages', 'No data'), result.get('year', 'No data'), result.get('summary', 'No data'), result.get('category', 'No data'), result.get('publisher', 'No data'), result.get('author', 'No data'))
        return book_found
   
    def create_many(self, books):
        client = self.__client_factory.get_client()
        db = client.bookStore
        db.books.insert_many(books)
        client.close()
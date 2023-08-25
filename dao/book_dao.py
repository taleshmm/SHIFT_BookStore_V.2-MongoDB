from model.book import Book

class BookDAO:
    def __init__(self):
        self.__books: list[Book] = list()
    
    def getAll(self) -> list[Book]:
        return self.__books
    
    def create(self, book: Book) -> None:
        self.__books.append(book)

    def delete(self, id: int) -> bool:
        found = False
        for book in self.__books:
            if book.id == id:
                index = self.__books.index(book)
                del self.__books[index]
                found = True
                break
        return found
    
    def getById(self, id: int) -> Book:
        book_found = None
        for book in self.__books:
            if book.id == id:
                book_found = book
                break
        return book_found
    
    def getLastId(self) -> int:
        if len(self.__books) != 0:
            return self.__books[-1].id
        else:
            return 0
    
    def getByTitle(self, title: str) -> Book:
        book_found = None
        for book in self.__books:
            if book.title == title:
                book_found = book
                break
        return book_found
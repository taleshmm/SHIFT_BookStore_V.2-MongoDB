from .author import Author
from .category import Category
from .publisher import Publisher
from bson import ObjectId

class Book:
    def __init__(self, title: str, isbn: str, pages: int, year: int,  summary: str, category: Category, publisher: Publisher, author: Author):
        self.__id: ObjectId = None
        self.__title: str = title
        self.__summary: str = summary
        self.__year: int = year
        self.__pages: int = pages
        self.__isbn: int = isbn
        self.__category: Category = category
        self.__publisher: Publisher = publisher
        self.__author: Author = author

    @property
    def id(self) -> ObjectId:
        return self.__id
    
    @id.setter
    def id(self, id: ObjectId):
        self.__id = id

    @property
    def title(self) -> str:
        return self.__title
    
    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def summary(self) -> str:
        return self.__summary
    
    @summary.setter
    def summary(self, summary: str):
        self.__summary = summary
    
    @property
    def year(self) -> int:
        return self.__year
    
    @year.setter
    def year(self, year: int):
        self.__year = year
   
    @property
    def pages(self) -> int:
        return self.__pages
    
    @pages.setter
    def pages(self, pages: int):
        self.__pages = pages
   
    @property
    def isbn(self) -> str:
        return self.__isbn
    
    @isbn.setter
    def isbn(self, isbn: str):
        self.__isbn = isbn
    
    @property
    def category(self) -> Category:
        return self.__category
    
    @category.setter
    def category(self, category: Category):
        self.__category = category
    
    @property
    def publisher(self) -> Publisher:
        return self.__publisher
    
    @publisher.setter
    def publisher(self, publisher: Publisher):
        self.__publisher = publisher
  
    @property
    def author(self) -> Author:
        return self.__author
    
    @author.setter
    def author(self, author: Author):
        self.__author = author
    
    def in_dump(self) -> dict:
      return {'title': self.__title, 'isbn': self.__isbn, 'pages': self.__pages, 'year': self.__year, 'summary': self.__summary, 'category': self.__category, 'publisher': self.__publisher, 'author': self.__author}
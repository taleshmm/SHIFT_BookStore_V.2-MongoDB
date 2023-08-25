from .author import Author
from .category import Category
from .editor import Editor

class Book:
    def __init__(self, id: int, title: str, summary: str, year: int, pages: int, isbn: str, category: Category, editor: Editor, author: Author):
        self.__id: int = id
        self.__title: str = title
        self.__summary: str = summary
        self.__year: int = year
        self.__pages: int = pages
        self.__isbn: int = isbn
        self.__category: Category = category
        self.__editor: Editor = editor
        self.__author: Author = author

    @property
    def id(self) -> int:
        return self.__id
    
    @id.setter
    def id(self, id: int):
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
    def editor(self) -> Editor:
        return self.__editor
    
    @editor.setter
    def editor(self, editor: Editor):
        self.__editor = editor
  
    @property
    def author(self) -> Author:
        return self.__author
    
    @author.setter
    def author(self, author: Author):
        self.__author = author
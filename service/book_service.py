from model.book import Book
from dao.book_dao import BookDAO
from model.category import Category
from dao.category_dao import CategoryDAO
from model.author import Author
from dao.author_dao import AuthorDAO
from model.publisher import Publisher
from dao.publisher_dao import PublisherDAO
from utils.csv_processor import read_csv_book, create_csv_book
from utils.json_processor import read_json_book, create_json_book
from utils.util import searchToName

class BookService:
    def __init__(self, category_dao: CategoryDAO, publisher_dao: PublisherDAO, author_dao: AuthorDAO):
      self.__book_dao = BookDAO()
      self.__category_dao: CategoryDAO = category_dao
      self.__publisher_dao:PublisherDAO = publisher_dao
      self.__author_dao: AuthorDAO = author_dao
       
    @property
    def book_dao(self) -> BookDAO:
       return self.__book_dao
    
    def menu(self):
      print('''\n[Books] Choose one of the following options:
      1 - List all books
      2 - Add a new book
      3 - Delete a book
      4 - View book by Id
      5 - Search by title
      6 - Read from CSV file
      7 - Export to CSV
      8 - Read from JSON file
      9 - Export to JSON
      10 - Insert file into the database
      0 - Back to the previous menu''')
         
      selection = input('Enter your choice: ')
      if selection == '0':
         return
      if selection == '1':
         self.listAll()
      elif selection == '2':
         self.add()
      elif selection == '3':
         self.remove()
      elif selection == '4':
         self.showById()
      elif selection == '5':
         self.showByTitle()
      elif selection == '6':
         self.read_file('CSV')
      elif selection == '7':
         self.export_to_file('CSV')
      elif selection == '8':
         self.read_file('JSON')
      elif selection == '9':
         self.export_to_file('JSON')
      elif selection == '10':
         self.insert_many() 
      else:
         print('Invalid option! Please try again!')

      self.menu()
 
    def listAll(self):
      print('\nListing all books...')
      try:
         books = self.__book_dao.getAll()
         if len(books) == 0:
            print('No books found!')
         for book in books:
            cat = self.__category_dao.getById(book.category)
            pub = self.__publisher_dao.getById(book.publisher)
            aut = self.__author_dao.getById(book.author)
            print(f'''ID: {book.id} | Title: {book.title.title()} | Year: {book.year} | Pages: {book.pages}
   Summary: {book.summary}
   Isbn: {book.isbn}
   Category: {cat.name.title() if cat else 'No data'}
   Publisher: {pub.name.title() if pub else 'No data'}
   Author: {aut.name.title() if aut else 'No data'}''')
      except Exception as e:
         print(f'Error displaying books! - {e}')
         return

      input('Press any key to continue...')

    def add(self):
      print('\nAdding a new book')
      try:
         title = input("Enter the title: ").title()
         summary = input("Enter the summary: ").capitalize()
         year = int(input("Enter the year: "))
         pages = int(input("Enter the number of pages: "))
         isbn = input("Enter the ISBN: ")
         
         print('\nBook Categories:')
         categories = self.__category_dao.getAll()
         for category in categories:
            print(f'ID: {category.id} | {category.name.capitalize()}')

         id = input('Enter the category ID: ')
         category_select: Category = self.__category_dao.getById(id)

         while category_select is None:
            print('Category does not exist')
            id = input('Enter the category ID: ')
            category_select: Category = self.__category_dao.getById(id)

         print('\nBook Publishers:')
         publishers = self.__publisher_dao.getAll()
         for publisher in publishers:
            print(f'ID {publisher.id} | Name: {publisher.name.capitalize()}')

         id = input('Enter the publisher ID: ')
         publisher_select: Publisher = self.__publisher_dao.getById(id)

         while publisher_select is None:
            print('Publisher does not exist')
            id = input('Enter the publisher ID: ')
            publisher_select: Publisher = self.__publisher_dao.getById(id)

         print('\nAuthors:')
         authors = self.__author_dao.getAll()
         for author in authors:
            print(f'ID: {author.id} | Name: {author.name.capitalize()}')

         id = input('Enter the author ID: ')
         author_select: Author = self.__author_dao.getById(id)

         while author_select is None:
            print('Author does not exist')
            id = input('Enter the author ID: ')
            author_select: Author = self.__author_dao.getById(id)

         new_book = Book(title, isbn, year, pages, summary, category_select.id, publisher_select.id, author_select.id)
         self.__book_dao.create(new_book)
         print('Book added successfully!')
      except Exception as e:
         print(f'Error adding book! - {e}')
         return
      input('Press any key to continue...')

    def remove(self):
      print('\nRemoving a book...')
      try:
         id = input("Enter the book ID to delete: ")
         if self.__book_dao.delete(id):
            print('Book deleted successfully')
         else:
            print('Book not found.')
      except Exception as e:
         print(f'Error deleting book! - {e}')
         return
      input('Press any key to continue...')

    def showById(self):
      print('\nBook by ID...')
      try:
         id = input('Enter the book ID: ')
         book = self.__book_dao.getById(id)
         if book is not None:
            cat = self.__category_dao.getById(book.category)
            pub = self.__publisher_dao.getById(book.publisher)
            aut = self.__author_dao.getById(book.author)
            print(f'''ID: {book.id} | Title: {book.title.title()} | Year: {book.year} | Pages: {book.pages}
   Summary: {book.summary}
   Isbn: {book.isbn}
   Category: {cat.name.title() if cat else 'No data'}
   Publisher: {pub.name.title() if pub else 'No data'}
   Author: {aut.name.title() if aut else 'No data'}''')
         else:
            print('Book not found.')
      except Exception as e:
         print(f'Error displaying book! - {e}')
         return
      input('Press any key to continue...')

    def showByTitle(self):
      print('\nBook by title...')
      try:
         title = input('Enter the book title: ')
         book = self.__book_dao.getByTitle(title)
         if book is not None:
            cat = self.__category_dao.getById(book.category)
            pub = self.__publisher_dao.getById(book.publisher)
            aut = self.__author_dao.getById(book.author)
            print(f'''ID: {book.id} | Title: {book.title.title()} | Year: {book.year} | Pages: {book.pages}
   Summary: {book.summary}
   Isbn: {book.isbn}
   Category: {cat.name.title() if cat else 'No data'}
   Publisher: {pub.name.title() if pub else 'No data'}
   Author: {aut.name.title() if aut else 'No data'}''')
         else:
            print('Book not found.')
      except Exception as e:
         print(f'Error displaying book! - {e}')
         return
      input('Press any key to continue...')
       
    def read_file(self, type_file: str):
      name_file = input(f'Enter the {type_file} file name (Must be in the project root).\n -> ')
      print(f'Listing from the {type_file} file...\n')
      try:
         books = None
         if type_file == 'CSV':
            books = read_csv_book(name_file)
         elif type_file == 'JSON':
            books = read_json_book(name_file)
         else:
            print('Unsupported file type.')
         for book in books:
            print(f'''ID: {book.id} | Title: {book.title.capitalize()} | Year: {book.year} | Pages: {book.pages}
   Summary: {book.summary}
   Isbn: {book.isbn}
   Category: {book.category}
   Publisher: {book.publisher}
   Author: {book.author}''')
      except Exception as e:
         print(f'Error displaying {type_file} file - {e}')
   
    def export_to_file(self, type_file: str):
      name_file = input(f'Enter the {type_file} file name: ')
      print(f'Creating {type_file} file... \n')
      try:
         books = self.__book_dao.getAll()
         if type_file == 'CSV':
            create_csv_book(name_file, books)
         elif type_file == 'JSON':
            create_json_book(name_file, books)
         else:
            print('Unsupported file type.')
      except Exception as e:
         print(f'Error creating {type_file} file - {e}')
     
    def insert_many(self):
      try:
         type_file = input('\nChoose the file type:\n 1 - CSV\n 2 - JSON\n-> ')
         name_file = input('Enter the file name: ')
         books_file = None
         if type_file == '1':
            books_file = read_csv_book(name_file)
         elif type_file == '2':
            books_file = read_json_book(name_file)
         else:
            print('Invalid option, please try again!')
            return
         list_books = list()
         print('Inserting into the database...\n')
         for bk in books_file:
            list_books.append({'title': bk.title, 'isbn': bk.isbn, 'pages': bk.pages, 'year': bk.year, 'summary': bk.summary, 'category': searchToName(self.__category_dao, bk.category), 'publisher': searchToName(self.__publisher_dao, bk.publisher), 'author': searchToName(self.__author_dao, bk.author)})
         self.__book_dao.create_many(list_books)
         print('Data inserted successfully.')
      except Exception as e:
         print(f'Error inserting data into the database - {e}')
         

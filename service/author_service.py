from dao.author_dao import AuthorDAO
from model.author import Author
from utils.util import showPhone, clearPhone
from utils.csv_processor import read_csv_author, create_csv_author
from utils.json_processor import read_json_author, create_json_author

class AuthorService:
    def __init__(self):
      self.__author_dao = AuthorDAO()
    
    @property
    def author_dao(self) -> AuthorDAO:
       return self.__author_dao
    
    def menu(self):
      print('''\n[Authors] Choose one of the following options:
      1 - List all authors
      2 - Add a new author
      3 - Delete an author
      4 - View author by Id
      5 - Search author by name
      6 - Search author by email
      7 - Read from CSV file
      8 - Export to CSV
      9 - Read from JSON file
      10 - Export to JSON
      11 - Insert file into the database
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
         self.showByName()
      elif selection == '6':
         self.showByEmail()
      elif selection == '7':
         self.read_file('CSV')
      elif selection == '8':
         self.export_to_file('CSV')
      elif selection == '9':
         self.read_file('JSON')
      elif selection == '10':
         self.export_to_file('JSON')
      elif selection == '11':
         self.insert_many()
      else:
         print('Invalid option! Please try again!')

      self.menu()
    
    def listAll(self):
      print('\nListing authors...')
      try:
         authors = self.__author_dao.getAll()
         if len(authors) == 0:
               print('No authors found!')
         for author in authors:
               print(f'{author.id} | {author.name.title()} | {author.email} | {showPhone(author.phone)} | {author.bio if author.bio is not None else "No data" }')
      except Exception as e:
         print(f'Error displaying authors! - {e}')
         return

      input('Press any key to continue... ')

    def add(self):
      print('\nAdding author')
      try:
         name = input("Enter the name: ").title()
         email = input("Enter the email: ").lower()
         phone  = clearPhone(input("Enter the phone number: "))
         bio = input("Enter the bio: ")

         new_author = Author(name, email, phone, bio)
         self.__author_dao.create(new_author)
         print('Author added successfully!')
      except Exception as e:
         print(f'Error while adding author! - {e}')
         return

      input('Press any key to continue... ')

    def remove(self):
      print('\nRemoving author...')
      try:
         id = int(input("Enter the ID to delete the author: "))
         if self.__author_dao.delete(id):
               print('Author deleted successfully.')
         else:
               print('Author not found.')
      except Exception as e:
         print(f'Error while deleting the author! - {e}')
         return

      input('Press any key to continue... ')

    def showById(self):
      print('\nAuthor by ID...')
      try:
         id = int(input('Enter the author ID: '))
         author = self.__author_dao.getById(id)
         if author is not None:
               print(f'ID: {author.id} | Name: {author.name.title()} \nEmail: {author.email} | Phone: {showPhone(author.phone)}\nBio: {author.bio if author.bio is not None else "No data"}')
         else:
               print('Author not found.')
      except Exception as e:
         print(f'Error displaying author! - {e}')
         return

      input('Press any key to continue...')

    def showByName(self):
      print('\nAuthor by name...')
      try:
         name = input('Enter the author name: ')
         author = self.__author_dao.getByName(name)
         if author is not None:
               print(f'ID: {author.id} | Name: {author.name.title()} \nEmail: {author.email} | Phone: {showPhone(author.phone)}\nBio: {author.bio if author.bio is not None else "No data"}')
         else:
               print('Author not found.')
      except Exception as e:
         print(f'Error displaying author! - {e}')
         return

      input('Press any key to continue...')

    def showByEmail(self):
      print('\nAuthor by email...')
      try:
         email = input('Enter the author email: ').lower()
         author = self.__author_dao.getByEmail(email)
         if author is not None:
               print(f'ID: {author.id} | Name: {author.name.title()} \nEmail: {author.email} | Phone: {showPhone(author.phone)}\nBio: {author.bio if author.bio is not None else "No data"}')
         else:
               print('Author not found.')
      except Exception as e:
         print(f'Error displaying author! - {e}')
         return

      input('Press any key to continue...')
       
    def read_file(self, type_file: str):
      name_file = input(f'Enter the {type_file} file name (Must be in the project root).\n -> ')
      print(f'Listing from {type_file} file...\n')
      try:
         authors = None
         if type_file == 'CSV':
               authors = read_csv_author(name_file)
         elif type_file == 'JSON':
               authors = read_json_author(name_file)
         else:
               print('Unsupported file type.')
         for author in authors: 
               print(f'ID: {author.id} | Name: {author.name.title()} \nEmail: {author.email} | Phone: {showPhone(author.phone)}\nBio: {author.bio if author.bio is not None else "No data"}')
      except Exception as e:
         print(f'Error displaying {type_file} file - {e}')

    def export_to_file(self, type_file:str):
      name_file = input(f'Enter the {type_file} file name: ')
      print(f'Creating {type_file} file... \n')
      try:
         authors = self.__author_dao.getAll()
         if type_file == 'CSV':
            create_csv_author(name_file, authors)
         elif type_file == 'JSON':
            create_json_author(name_file, authors)
         else:
            print('Unsupported file type.')
      except Exception as e:
         print(f'Error creating {type_file} file - {e}')

    def insert_many(self):
      try:
         type_file = input(' \nChoose the file type:\n 1 - CSV\n 2 - JSON\n-> ')
         name_file = input('Enter the file name: ')
         authors_file = None
         if type_file == '1':
            authors_file = read_csv_author(name_file)
         elif type_file == '2':
            authors_file = read_json_author(name_file)
         else: 
            print('Invalid option, please try again!')
            return
         list_authors = list()
         print('Inserting into the database...\n')
         for at in authors_file:
            list_authors.append((at.name, at.email, at.phone, at.bio))
         self.__author_dao.create_many(list_authors)
         print('Data inserted successfully.')
      except Exception as e:
         print(f'Error inserting data into the database - {e}')

     

    
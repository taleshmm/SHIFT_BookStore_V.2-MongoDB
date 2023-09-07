from dao.publisher_dao import PublisherDAO
from model.publisher import Publisher
from utils.util import showPhone, clearPhone
from utils.csv_processor import read_csv_publisher, create_csv_publisher
from utils.json_processor import read_json_publisher, create_json_publisher

class PublisherService:
    def __init__(self):
      self.__publisher_dao = PublisherDAO()
    
    @property
    def publisher_dao(self) -> PublisherDAO:
       return self.__publisher_dao
    
    def menu(self):
      print('''\n[Publishers] Choose one of the following options:
      1 - List all publishers
      2 - Add a new publisher
      3 - Delete a publisher
      4 - View a publisher by ID
      5 - Search for a publisher by name
      6 - Read from CSV file
      7 - Export to CSV file
      8 - Read from JSON file
      9 - Export to JSON file
      10 - Insert file into the database
      0 - Return to the previous menu''')

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
      print('\nListing publishers...')
      try:
         publishers = self.__publisher_dao.getAll()
         if len(publishers) == 0:
            print('No publishers found!')
         else:
            print('ID | Name  | Phone |   Address')
            for publisher in publishers:
               print(f'{publisher.id} | {publisher.name.title()} | {showPhone(publisher.phone)} | {publisher.address.title()}')
      except Exception as e:
         print(f'Error while displaying publishers! - {e}')
         return
      input('Press any key to continue...')

    def add(self):
      print('\nAdding publisher...')
      try:
         name = input('Enter the publisher name: ').title()
         phone = input('Enter the phone number: ')
         address = input('Enter the address: ').title()
         new_publisher = Publisher(name, address, clearPhone(phone))
         self.__publisher_dao.create(new_publisher)
         print('Publisher added successfully!')
      except Exception as e:
         print(f'Error while adding publisher! - {e}')
         return
      input('Press any key to continue...')
     
    def remove(self):
      print('\nRemoving publisher...')
      try:
         id = input('Enter the ID of the publisher you want to delete: ')
         if self.__publisher_dao.delete(id):
            print('Publisher deleted successfully!')
         else:
            print('Publisher not found')
      except Exception as e:
         print(f'Error while deleting publisher! - {e}')
         return
      input('Press any key to continue...')

    def showById(self):
      print('\nPublisher by ID...')
      try:
         id = input('Enter the ID of the publisher: ')
         publisher = self.__publisher_dao.getById(id)
         if publisher is not None:
            print(f'ID: {publisher.id} | Name: {publisher.name.title()} | Address: {publisher.address} | Phone: {showPhone(publisher.phone)}')
         else:
            print('Publisher not found!')
      except Exception as e:
         print(f'Error while displaying publisher! - {e}')
         return
      input('Press any key to continue...')

    def showByName(self):
      print('\nPublisher by name...')
      try:
         name = input('Enter the name of the publisher: ').title()
         publisher = self.__publisher_dao.getByName(name)
         if publisher is not None:
            print(f'ID: {publisher.id} | Name: {publisher.name.title()} | Address: {publisher.address} | Phone: {showPhone(publisher.phone)}')
         else:
            print('Publisher not found!')
      except Exception as e:
         print(f'Error while displaying publisher! - {e}')
         return
      input('Press any key to continue...')

    def read_file(self, type_file: str):
      name_file = input(f'Enter the name of the {type_file} file (Must be in the project root).\n -> ')
      print(f'Reading from {type_file} file...\n')
      try:
         publishers = None
         if type_file == 'CSV':
            publishers = read_csv_publisher(name_file)
         elif type_file == 'JSON':
            publishers = read_json_publisher(name_file)
         else:
            print('Unsupported file type.')  
         for publisher in publishers: 
            print(f'Name: {publisher.name.title()} | Address: {publisher.address} | Phone: {showPhone(publisher.phone)}')
      except Exception as e:
         print(f'Error while displaying {type_file} file - {e}')
          
    def showByName(self):
      print('\nPublisher by name...')
      try:
         name = input('Enter the name of the publisher: ').title()
         publisher = self.__publisher_dao.getByName(name)
         if publisher is not None:
            print(f'ID: {publisher.id} | Name: {publisher.name.title()} | Address: {publisher.address} | Phone: {showPhone(publisher.phone)}')
         else:
            print('Publisher not found!')
      except Exception as e:
         print(f'Error while displaying publisher! - {e}')
         return
      input('Press any key to continue...')

    def read_file(self, type_file: str):
      name_file = input(f'Enter the name of the {type_file} file (Must be in the project root).\n -> ')
      print(f'Reading from {type_file} file...\n')
      try:
         publishers = None
         if type_file == 'CSV':
            publishers = read_csv_publisher(name_file)
         elif type_file == 'JSON':
            publishers = read_json_publisher(name_file)
         else:
            print('Unsupported file type.')  
         for publisher in publishers: 
            print(f'Name: {publisher.name.title()} | Address: {publisher.address} | Phone: {showPhone(publisher.phone)}')
      except Exception as e:
         print(f'Error while displaying {type_file} file - {e}')

    def export_to_file(self, file_type: str):
      file_name = input(f'Enter the {file_type} file name: ')
      print(f'Creating {file_type} file... \n')
      try:
         publishers = self.__publisher_dao.getAll()
         if file_type == 'CSV':
            create_csv_publisher(file_name, publishers)
         elif file_type == 'JSON':
            create_json_publisher(file_name, publishers)
         else:
             print('Unsupported file type.')
      except Exception as e:
         print(f'Error creating {file_type} file - {e}')

    def insert_many(self):
      try:
         file_type = input(' \nChoose the file type:\n 1 - CSV\n 2 - JSON\n-> ')
         file_name = input('Enter the file name: ')
         publishers_file = None
         if file_type == '1':
            publishers_file = read_csv_publisher(file_name)
         elif file_type == '2':
            publishers_file = read_json_publisher(file_name)
         else:
            print('Invalid option, please try again!')
            return
         list_publishers = list()
         print('Inserting into the database...\n')
         for publisher in publishers_file:            
            list_publishers.append({'name': publisher.name, 'address': publisher.address, 'phone': publisher.phone})
         self.__publisher_dao.create_many(list_publishers)
         print('Data inserted successfully.')
      except Exception as e:
         print(f'Error inserting data into the database - {e}')

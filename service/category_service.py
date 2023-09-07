from dao.category_dao import CategoryDAO
from model.category import Category
from utils.csv_processor import read_csv_category, create_csv_category
from utils.json_processor import read_json_category, create_json_category

class CategoryService:
  def  __init__ (self):
   self.__category_dao: CategoryDAO = CategoryDAO()

  @property
  def category_dao(self) -> CategoryDAO:
    return self.__category_dao
   
  def menu(self):
     print('''\n[Categories] Choose one of the following options:
     1 - List all categories
     2 - Add a new category
     3 - Delete a category
     4 - View category by Id
     5 - Search category by name
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
    print('\nListing categories...')
    try:
      categories = self.__category_dao.getAll()
      if len(categories) == 0:
        print('No categories found!')
      for category in categories:
        print(f'{category.id} | {category.name.title()}')
    except Exception as e:
        print(f'Error while displaying categories! - {e}')
        return
    input('Press any key to continue... ')

  def add(self):
    print('\nAdding category...')
    try:
      name = input('Enter the category name: ').title()
      new_category = Category(name)
      self.__category_dao.create(new_category)
      print('Category added successfully!')
    except Exception as e:
      print(f'Error while inserting category! - {e}')
      return
    input('Press any key to continue... ')

  def remove(self):
    print('\nRemoving category...')
    try:
      category_id = input('Enter the category ID to delete: ')
      if self.__category_dao.delete(category_id):
          print('Category deleted successfully!')
      else:
          print('Category not found.')
    except Exception as e:
      print(f'Error while deleting category! - {e}')
      return
    input('Press any key to continue... ')

  def showById(self):
    print('\nCategory by Id...')
    try:
      id = input('Enter the category ID: ')
      category = self.__category_dao.getById(id)
      if category is not None: 
          print(f'ID: {category.id} | Name: {category.name.title()}')
      else:
          print('Category not found')
    except Exception as e:
      print(f'Error while displaying category! - {e}')
      return   
    input('Press any key to continue...' )

  def showByName(self):
    print('\nCategory by name...')  
    try:
      name = input('Enter the category name: ').title()
      category = self.__category_dao.getByName(name)
      if category is not None: 
          print(f'ID: {category.id} | Name: {category.name.title()}')
      else:
          print('Category not found')
    except Exception as e:
      print(f'Error while displaying category! - {e}')
      return   
    input('Press any key to continue... ')

  def read_file(self, type_file: str):
    name_file = input(f'Enter the name of the {type_file} file (Needs to be in the root of the project). \n -> ')
    print(f'Listing from {type_file} file...\n')
    try:
      categories = None
      if type_file == 'CSV':
        categories = read_csv_category(name_file)
      elif type_file == 'JSON':
        categories = read_json_category(name_file)
      else:
        print('Unsupported file type.')  
      for cat in categories: 
        print(f'Name: {cat.name.title()}')
    except Exception as e:
      print(f'Error while displaying {type_file} file - {e}')

  def export_to_file(self, type_file: str):
    name_file = input(f'Enter the name of the {type_file} file: ')
    print(f'Creating {type_file} file... \n')
    try:
      categories = self.__category_dao.getAll()
      if type_file == 'CSV':
        create_csv_category(name_file, categories)
      elif type_file == 'JSON':
        create_json_category(name_file, categories)
      else:
        print('Unsupported file type.')
    except Exception as e:
      print(f'Error while creating {type_file} file - {e}')
 
  def insert_many(self):
    try:
      type_file = input(' \nChoose the file type:\n 1 - CSV\n 2 - JSON\n-> ')
      name_file = input('Enter the file name: ')
      categories_file = None
      if type_file == '1':
        categories_file = read_csv_category(name_file)
      elif type_file == '2':
        categories_file = read_json_category(name_file)
      else: 
        print('Invalid option, please try again!')
        return
      list_categories = list()
      print('\nInserting into the database...\n')
      for cat in categories_file:
          list_categories.append({'name': cat.name})
      self.__category_dao.create_many(list_categories)
      print('Data inserted successfully.')
    except Exception as e:
      print(f'Error while inserting data into the database - {e}')

       
      
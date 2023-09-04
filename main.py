from service.category_service import CategoryService
from service.publisher_service import PublisherService
from service.author_service import AuthorService
from service.book_service import BookService

category_service = CategoryService()
publisher_service = PublisherService()
author_service = AuthorService()
book_service = BookService(category_service.category_dao, publisher_service.publisher_dao, author_service.author_dao)

def main_menu():
    print('''\n[Main Menu] Choose one of the following options:
  1 - Categories
  2 - Publishers
  3 - Authors
  4 - Books
  0 - Exit the program''')
    selection = input('Enter your choice: ')

    if selection == '0':
        print('Thank you, goodbye!')
        return
    if selection == '1':
        category_service.menu()
    elif selection == '2':
        publisher_service.menu()
    elif selection == '3':
        author_service.menu()
    elif selection == '4':
        book_service.menu()
    else:
        print('Invalid option! Please, try again.')

    main_menu()

if __name__ == '__main__':
    print('Welcome to SHIFT Bookstore - Mastering Python!')
    main_menu()



      

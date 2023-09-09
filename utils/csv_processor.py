import csv
from pathlib import Path
from model.publisher import Publisher
from model.category import Category
from model.author import Author
from model.book import Book
from dao.category_dao import CategoryDAO
from dao.author_dao import AuthorDAO
from dao.publisher_dao import PublisherDAO
from .util import searchToId


def get_path_complet(name_file: str) -> str:
  return f'{str(Path().absolute())}/{name_file}.csv'

def read_csv_publisher(name_file: str):
  with open(get_path_complet(name_file)) as file_csv:
    csv_reader = csv.DictReader(file_csv, delimiter=',') 
    list_publishers = list()
    for row in csv_reader:
      row_changed = Publisher(row['name'], row['address'], row['phone'])
      list_publishers.append(row_changed)
    return list_publishers
  
def read_csv_author(name_file: str):
  with open(get_path_complet(name_file)) as file_csv:
    csv_reader = csv.DictReader(file_csv, delimiter=',') 
    list_authors = list()
    for row in csv_reader:
      row_changed = Author(row['name'], row['email'], row['phone'], row['bio'])
      list_authors.append(row_changed)
    return list_authors
  
def read_csv_category(name_file: str):
  with open(get_path_complet(name_file)) as file_csv:
    csv_reader = csv.DictReader(file_csv, delimiter=',') 
    list_categories = list()
    for row in csv_reader:
      row_changed = Category(row['name'])
      list_categories.append(row_changed)
    return list_categories
  
def read_csv_book(name_file: str):
  with open(get_path_complet(name_file)) as file_csv:
    csv_reader = csv.DictReader(file_csv, delimiter=',') 
    list_books = list()
    for row in csv_reader:
      row_changed = Book(row['title'], row['isbn'], row['year'], row['pages'],row['summary'], row['category'], row['publisher'], row['author'])
      list_books.append(row_changed)
    return list_books
  
def create_csv_publisher(name_file: str, list_publishers):
  with open(get_path_complet(name_file), 'w', newline='') as new_file:
    new_publisher = csv.writer(new_file)
    new_publisher.writerow(['name', 'address', 'phone'])
    for publisher in list_publishers:
      new_publisher.writerow([publisher.name, publisher.address, publisher.phone])
  print('---Data has been loaded successfully!---')

def create_csv_author(name_file: str, list_authors):
  with open(get_path_complet(name_file), 'w', newline='') as new_file:
    new_author = csv.writer(new_file)
    new_author.writerow(['name', 'email', 'phone', 'bio'])
    for author in list_authors:
      new_author.writerow([author.name, author.email, author.phone, author.bio])
  print('---Data has been loaded successfully!---')

def create_csv_category(name_file: str, list_categorys):
  with open(get_path_complet(name_file), 'w', newline='') as new_file:
    new_category = csv.writer(new_file)
    new_category.writerow(['name'])
    for category in list_categorys:
      new_category.writerow([category.name])
  print('---Data has been loaded successfully!---')

def create_csv_book(name_file: str, list_books):
  publisher_dao = PublisherDAO()
  author_dao = AuthorDAO()
  category_dao = CategoryDAO()
  with open(get_path_complet(name_file), 'w', newline='') as new_file:
    new_book = csv.writer(new_file)
    new_book.writerow(['title', 'isbn', 'year', 'pages', 'summary', 'category', 'publisher', 'author'])
    for book in list_books:
      new_book.writerow([book.title, book.isbn, book.year, book.pages, book.summary, searchToId(category_dao, book.category), searchToId(publisher_dao, book.publisher), searchToId(author_dao, book.author)])
  print('---Data has been loaded successfully!---')

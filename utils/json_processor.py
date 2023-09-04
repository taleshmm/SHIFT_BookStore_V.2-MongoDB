import json
from pathlib import Path
from model.publisher import Publisher
from model.category import Category
from model.author import Author
from model.book import Book


def get_path_complet(name_file: str) -> str:
  return f'{str(Path().absolute())}/{name_file}.json'

def read_json_publisher(name_file: str):
  with open(get_path_complet(name_file)) as file_json:
    json_reader = json.load(file_json) 
    list_publishers = list()
    for row in json_reader:
      row_changed = Publisher(row['name'], row['address'], row['phone'])
      list_publishers.append(row_changed)
    return list_publishers
  
def read_json_author(name_file: str):
  with open(get_path_complet(name_file)) as file_json:
    json_reader = json.load(file_json) 
    list_authors = list()
    for row in json_reader:
      row_changed = Author(row['name'], row['email'], row['phone'], row['bio'])
      list_authors.append(row_changed)
    return list_authors
  
def read_json_category(name_file: str):
  with open(get_path_complet(name_file)) as file_json:
    json_reader = json.load(file_json) 
    list_categories = list()
    for row in json_reader:
      row_changed = Category(row['name'])
      list_categories.append(row_changed)
    return list_categories
  
def read_json_book(name_file: str):
  with open(get_path_complet(name_file)) as file_json:
    json_reader = json.load(file_json) 
    list_books = list()
    for row in json_reader:
      row_changed = Book(row['title'], row['isbn'], row['year'], row['pages'],row['summary'], row['category'], row['publisher'], row['author'])
      list_books.append(row_changed)
    return list_books
  
def create_json_publisher(name_file: str, list_publishers) -> None:
  with open(get_path_complet(name_file), 'w', newline='') as new_file:
    new_list_publisher = list()
    for row in list_publishers:
      new_list_publisher.append(row.in_dump())
    json.dump(new_list_publisher, new_file, ensure_ascii=False, indent=4)
  print('---Data has been loaded successfully!---')


def create_json_author(name_file: str, list_authors) -> None:
  with open(get_path_complet(name_file), 'w', newline='') as new_file:
    new_list_author = list()
    for row in list_authors:
      new_list_author.append(row.in_dump())
    json.dump(new_list_author, new_file, ensure_ascii=False, indent=4)
  print('---Data has been loaded successfully!---')

def create_json_category(name_file: str, list_categorys) -> None:
  with open(get_path_complet(name_file), 'w', newline='') as new_file:
    new_list_category = list()
    for row in list_categorys:
      new_list_category.append(row.in_dump())
    json.dump(new_list_category, new_file, ensure_ascii=False, indent=4)
  print('---Data has been loaded successfully!---')

def create_json_book(name_file: str, list_books) -> None:
  with open(get_path_complet(name_file), 'w', newline='') as new_file:
    new_list_book = list()
    for row in list_books:
      new_list_book.append(row.in_dump())
    json.dump(new_list_book, new_file, ensure_ascii=False, indent=4)
  print('---Data has been loaded successfully!---')

import csv
from pathlib import Path
from model.editor import Editor
from model.author import Author
from model.category import Category
from model.book import Book


def get_path_complet(name_file: str) -> str:
  return f'{str(Path().absolute())}/{name_file}.csv'

def read_csv_editor(name_file: str) -> list(Editor):
  with open(get_path_complet(name_file)) as file_csv:
    csv_reader = csv.DictReader(file_csv, delimiter=',') 
    list_editors = list()
    for row in csv_reader:
      editorRow = Editor(row['name'], row['address'], row['phone'])
      list_editors.append(editorRow)
    return list_editors
  
def read_csv_author(name_file: str) -> list(Editor):
  with open(get_path_complet(name_file)) as file_csv:
    csv_reader = csv.DictReader(file_csv, delimiter=',') 
    list_authors = list()
    for row in csv_reader:
      editorRow = Author(row['name'], row['email'], row['phone'], row['bio'])
      list_authors.append(editorRow)
    return list_authors
  
def read_csv_category(name_file: str) -> list(Editor):
  with open(get_path_complet(name_file)) as file_csv:
    csv_reader = csv.DictReader(file_csv, delimiter=',') 
    list_categories = list()
    for row in csv_reader:
      editorRow = Category(row['name'])
      list_categories.append(editorRow)
    return list_categories
  
def read_csv_book(name_file: str) -> list(Editor):
  with open(get_path_complet(name_file)) as file_csv:
    csv_reader = csv.DictReader(file_csv, delimiter=',') 
    list_books = list()
    for row in csv_reader:
      editorRow = Book(row['title'], row['isbn'], row['year'], row['pages'],row['summary'], row['category'], row['editor'], row['author'])
      list_books.append(editorRow)
    return list_books
  
def create_csv_editor(name_file: str, list_editors: list(Editor)):
  with open(get_path_complet(name_file), 'w', newline='') as new_file:
    new_editor = csv.writer(new_file)
    new_editor.writerow(['name', 'address', 'phone'])
    for editor in list_editors:
      new_editor.writerow([editor.name, editor.address, editor.phone])
  print('Os dados foram carregados com sucesso!')

def create_csv_author(name_file: str, list_authors: list(Author)):
  with open(get_path_complet(name_file), 'w', newline='') as new_file:
    new_author = csv.writer(new_file)
    new_author.writerow(['name', 'email', 'phone', 'bio'])
    for author in list_authors:
      new_author.writerow([author.name, author.email, author.phone, author.bio])
  print('Os dados foram carregados com sucesso!')

def create_csv_category(name_file: str, list_categorys: list(Category)):
  with open(get_path_complet(name_file), 'w', newline='') as new_file:
    new_category = csv.writer(new_file)
    new_category.writerow(['name'])
    for category in list_categorys:
      new_category.writerow([category.name])
  print('Os dados foram carregados com sucesso!')

def create_csv_book(name_file: str, list_books: list(Book)):
  with open(get_path_complet(name_file), 'w', newline='') as new_file:
    new_book = csv.writer(new_file)
    new_book.writerow(['title', 'isbn', 'year', 'pages', 'summary', 'category', 'editor', 'author'])
    for book in list_books:
      new_book.writerow([book.title, book.isbn, book.year, book.pages, book.summary, book.category, book.editor, book.author])
  print('Os dados foram carregados com sucesso!')


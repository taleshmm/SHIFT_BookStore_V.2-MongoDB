from model.book import Book
from dao.book_dao import BookDAO
from model.category import Category
from dao.category_dao import CategoryDAO
from model.author import Author
from dao.author_dao import AuthorDAO
from model.editor import Editor
from dao.editor_dao import EditorDAO
from utils.csv_processor import read_csv_book, create_csv_book
from utils.json_processor import read_json_book, create_json_book

class BookService:
    def __init__(self, category_dao: CategoryDAO, editor_dao: EditorDAO, author_dao: AuthorDAO):
      self.__book_dao = BookDAO()
      self.__category_dao: CategoryDAO = category_dao
      self.__editor_dao:EditorDAO = editor_dao
      self.__author_dao: AuthorDAO = author_dao
      
    
    @property
    def book_dao(self) -> BookDAO:
       return self.__book_dao
    
    def menu(self):
        print('''\n[Livros] Escolha uma das seguintes opções:
     1 - Listar todos os livros
     2 - Adicionar novo livro
     3 - Excluir livro
     4 - Ver livro por Id
     5 - Pesquisar por título
     6 - Ler de arquivo CSV
     7 - Exportar para CSV
     8 - Ler de arquivo JSON
     9 - Exportar para JSON
     10 - Inserir arquivo no banco
     0 - Voltar ao menu anterior''')
        
        selection = input('Digite a opção: ')
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
           print('Opção inválida! Por favor, tente novamente!')
     
        self.menu()
    
    def listAll(self):
       print('\nListando os livros)...')

       try:
          books = self.__book_dao.getAll()
          if len(books) == 0:
             print('Nenhum livro encontrado!')
          for book in books:
             print(f'''ID: {book.id} | Título: {book.title.title()} | Ano: {book.year} | Páginas: {book.pages}
Resumo: {book.summary}
Isbn: {book.isbn}
Categoria: {self.__category_dao.getById(book.category).name.title()}
Editora: {self.__editor_dao.getById(book.editor).name.title()}
Autor(a): {self.__author_dao.getById(book.author).name.title()}''')
       except Exception as e:
         print(f'Erro ao exibir os livros! - {e}')
         return
    
       input('Pressione uma tecla para continuar... ')


    def add(self):
      print('\nAdicionando autor(a)')
      try:
        title = input("Digite o título: ").title()
        summary = input("Digite a sinopse: ").capitalize()
        year  = int(input("Digite o ano: "))
        pages = int(input("Digite a páginas: "))
        isbn = input("Digite o isbn: ")
        
        print('\nCategorias de livros:')
        categorys = self.__category_dao.getAll()
        for category in categorys:
           print(f'ID: {category.id} | {category.name.capitalize()}')
       
        id = int(input('Digite o ID da categoria: '))
        category_select: Category = self.__category_dao.getById(id)
        
        while category_select == None:
         print('Categoria não existente')
         id = int(input('Digite o ID da categoria: '))
         category_select: Category = self.__category_dao.getById(id)
         
         
        print('\nEditoras de livros: ')
        editors = self.__editor_dao.getAll()
        for ed in editors:
          print(f'ID {ed.id} | Nome: {ed.name.capitalize()}') 
        
        id = int(input('Digite o ID da editora: '))
        editor_select: Editor = self.__editor_dao.getById(id)
        
        while editor_select == None:
         print('Editora não existente')
         id = int(input('Digite o ID da editora: '))
         editor_select: Editor = self.__editor_dao.getById(id)
       
        print('\nAutores(as): ')
        authors = self.__author_dao.getAll()
        for a in authors:
           print(f'ID: {a.id} | Nome: {a.name.capitalize()}')
         
        id = int(input('Digite o ID do autor(a): '))
        author_select: Author = self.__author_dao.getById(id)
        
        while author_select == None:
         print('Autor(a) não existente')
         id = int(input('Digite o ID do autor(a): '))
         author_select: Author = self.__author_dao.getById(id)
         
        new_book = Book(title, isbn , year, pages, summary, category_select.id, editor_select.id, author_select.id)
        self.__book_dao.create(new_book)    
        print('Livro adicionado com sucesso!')
      except Exception as e:
        print(f'Erro ao adicionar livro! - {e}')
        return
    
      input('Pressione uma tecla para continuar... ')

    def remove(self):
      print('\nRemovendo livro...')
      try:
         id = int(input("Digite o ID para deletar o livro): "))
         if self.__book_dao.delete(id):
            print('Livro excluído(a) com sucesso')
         else:
            print('Livro não encontrado.')
      except Exception as e:
        print(f'Erro ao deletar livro! - {e}')
        return
    
      input('Pressione uma tecla para continuar... ')

    def showById(self):
       print('\nLivro por ID...')
       try:
          id = int(input('Digite o ID do autor(a): '))
          book = self.__book_dao.getById(id)
          if book is not None:
            print(f'''ID: {book.id} | Título: {book.title.title()} | Ano: {book.year} | Páginas: {book.pages}
Resumo: {book.summary}
Isbn: {book.isbn}
Categoria: {self.__category_dao.getById(book.category).name.title()}
Editora: {self.__editor_dao.getById(book.editor).name.title()}
Autor(a): {self.__author_dao.getById(book.author).name.title()}''')
          else:
             print('Livro não encontrado.')
       except Exception as e:
        print(f'Erro ao exibir livro! - {e}')
        return   
    
       input('Pressione uma tecla para continuar...' )


    def showByTitle(self):
      print('\nLivro por título...')
      try:
         title = input('Digite o titulo do livro: ')
         book = self.__book_dao.getByTitle(title)
         if book is not None:
          print(f'''ID: {book.id} | Título: {book.title.capitalize()} | Ano: {book.year} | Páginas: {book.pages}
 Resumo: {book.summary}
 Isbn: {book.isbn}
 Categoria: {self.__category_dao.getById(book.category).name.title()}
 Editora: {self.__editor_dao.getById(book.editor).name.title()}
 Autor(a): {self.__author_dao.getById(book.author).name.title()}''')
         else:
           print('Livro não encontrado.')
      except Exception as e:
        print(f'Erro ao exibir livro! - {e}')
        return   
    
      input('Pressione uma tecla para continuar...' )
         
    def read_file(self, type_file: str):
      name_file = input(f'Digite o nome do arquivo {type_file} (Precisa estar na raiz do projeto). \n -> ')
      print(f'Listando do arquivo {type_file}...\n')
      try:
         books = None
         if type_file == 'CSV':
            books = read_csv_book(name_file)
         elif type_file == 'JSON':
            books = read_json_book(name_file)
         else:
            print('O tipo de arquivo diferentes do suportado.')  
         for book in books: 
            print(f'''ID: {book.id} | Título: {book.title.capitalize()} | Ano: {book.year} | Páginas: {book.pages}
 Resumo: {book.summary}
 Isbn: {book.isbn}
 Categoria: {book.category}
 Editora: {book.editor}
 Autor(a): {book.author}''')
      except Exception as e:
         print(f'Error ao exibir arquivo {type_file} - {e}')
         
    def export_to_file(self, type_file:str):
      name_file = input(f'Digite o nome do arquivo {type_file}: ')
      print(f'Criando arquivo {type_file}... \n')
      try:
         books = self.__book_dao.getAll()
         if type_file == 'CSV':
            create_csv_book(name_file, books)
         elif type_file == 'JSON':
            create_json_book(name_file, books)
         else:
            print('O tipo de arquivo diferentes do suportado.')
      except Exception as e:
         print(f'Error ao criar arquivo {type_file} - {e}')   
         
    def insert_many(self):
     try:
      type_file = input(' \nEscolha o tipo de arquivo:\n 1 - CSV\n 2 - JSON\n-> ')
      name_file = input('Digite o nome do arquivo: ')
      books_file = None
      if type_file == '1':
        books_file = read_csv_book(name_file)
      elif type_file == '2':
        books_file = read_json_book(name_file)
      else: 
        print('Opção inválida, tente novamente!')
        return
      list_books = list()
      print('Inserindo em banco...\n')
      for bk in books_file:
         list_books.append((bk.title, bk.isbn, bk.pages, bk.year, bk.summary, bk.category, bk.editor, bk.author))
      self.__book_dao.create_many(list_books)
      print('Dados inseridos com sucesso.')
     except Exception as e:
       print(f'Error ao inserir dados no banco - {e}')
  

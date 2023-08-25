from model.book import Book
from dao.book_dao import BookDAO
from model.category import Category
from dao.category_dao import CategoryDAO
from model.author import Author
from dao.author_dao import AuthorDAO
from model.editor import Editor
from dao.editor_dao import EditorDAO

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
        else:
           print('Opção inválida! Por favor, tente novamente!')
     
        self.menu()
    
    def listAll(self):
       print('\nListando os livros)...')

       try:
          books = self.__book_dao.getAll()
          if len(books) == 0:
             print('Nenhum autor(a) encontrada!')
          for book in books:
             print(f'''ID: {book.id} | Título: {book.title.capitalize()} | Ano: {book.year} | Páginas: {book.pages}
   Resumo: {book.summary}
   Isbn: {book.isbn}
   Categoria: {book.category.name.capitalize()}
   Editora: {book.editor.name.capitalize()}
   Autor(a): {book.author.name.capitalize()}''')
       except Exception as e:
         print(f'Erro ao exibir as autores(as)! - {e}')
         return
    
       input('Pressione uma tecla para continuar... ')


    def add(self):
      print('\nAdicionando autor(a)')
      try:
        id = self.__book_dao.getLastId() + 1
        title = input("Digite o título: ").lower()
        summary = input("Digite a sinopse: ").lower()
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
         
        new_book = Book(id, title, summary, year, pages, isbn, category_select, editor_select, author_select)
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
            print(f'''ID: {book.id} | Título: {book.title.capitalize()} | Ano: {book.year} | Páginas: {book.pages}
   Resumo: {book.summary}
   Isbn: {book.isbn}
   Categoria: {book.category.name.capitalize()}
   Editora: {book.editor.name.capitalize()}
   Autor(a): {book.author.name.capitalize()}''')
          else:
             print('Livro não encontrado.')
       except Exception as e:
        print(f'Erro ao exibir livro! - {e}')
        return   
    
       input('Pressione uma tecla para continuar...' )


    def showByTitle(self):
      print('\nLivro por título...')
      try:
         title = input('Digite o titulo do livro: ').lower()
         book = self.__book_dao.getByTitle(title)
         if book is not None:
          print(f'''ID: {book.id} | Título: {book.title.capitalize()} | Ano: {book.year} | Páginas: {book.pages}
   Resumo: {book.summary}
   Isbn: {book.isbn}
   Categoria: {book.category.name.capitalize()}
   Editora: {book.editor.name.capitalize()}
   Autor(a): {book.author.name.capitalize()}''')
         else:
           print('Livro não encontrado.')
      except Exception as e:
        print(f'Erro ao exibir livro! - {e}')
        return   
    
      input('Pressione uma tecla para continuar...' )

   

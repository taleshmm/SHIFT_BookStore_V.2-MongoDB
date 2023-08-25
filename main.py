from service.category_service import CategoryService
from service.editor_service import EditorService
from service.author_service import AuthorService
from service.book_service import BookService

category_service = CategoryService()
editor_service = EditorService()
author_service = AuthorService()
book_service = BookService(category_service.category_dao, editor_service.editor_dao, author_service.author_dao)

def principal_menu():
     print('''\n[Menu Principal] Escolha uma das seguintes opções:
  1 - Categorias
  2 - Editoras
  3 - Autores(as)
  4 - Livros
  0 - Sair do programa''')
     selection = input('Digite a opção: ')
     
     if selection == '0':
        print('Obrigado, até logo!')
        return
     if selection == '1':
        category_service.menu()
     elif selection == '2':
         editor_service.menu()
     elif selection == '3':
         author_service.menu()
     elif selection == '4':
         book_service.menu()
     else:
        print('Opção inválida! Por favor, tente novamente!')
     
     principal_menu() 

if __name__ == '__main__':
    print('Bem-vindo a Livraria SHIFT - Mastering Python!')
    principal_menu()


      

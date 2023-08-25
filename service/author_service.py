from dao.author_dao import AuthorDAO
from model.author import Author
from utils.util import showPhone, clearPhone

class AuthorService:
    def __init__(self):
      self.__author_dao = AuthorDAO()
    
    @property
    def author_dao(self) -> AuthorDAO:
       return self.__author_dao
    
    def menu(self):
        print('''\n[Autores] Escolha uma das seguintes opções:
     1 - Listar todas os autores(as)
     2 - Adicionar nova autor(a)
     3 - Excluir autor(a)
     4 - Ver autor(a) por Id
     5 - Pesquisar autor(a) por nome
     6 - Pesquisar autor(a) por e-mail
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
           self.showByName()
        elif selection == '6':
           self.showByEmail()
        else:
           print('Opção inválida! Por favor, tente novamente!')
     
        self.menu()
    
    def listAll(self):
       print('\nListando os autores(as)...')

       try:
          authors = self.__author_dao.getAll()
          if len(authors) == 0:
             print('Nenhum autor(a) encontrada!')
          for author in authors:
             print(f'{author.id} | {author.name.capitalize()} | {author.email} | {showPhone(author.phone)} | {author.bio}')
       except Exception as e:
         print(f'Erro ao exibir as autores(as)! - {e}')
         return
    
       input('Pressione uma tecla para continuar... ')


    def add(self):
      print('\nAdicionando autor(a)')
      try:
        id = self.__author_dao.getLastId() + 1
        name = input("Digite o nome: ").lower()
        email = input("Digite o e-mail: ").lower()
        phone  = clearPhone(input("Digite o telefone: "))
        bio = input("Digite a bio: ")

        new_author = Author(id, name, email, phone, bio)
        self.__author_dao.create(new_author)
        print('Autor(a) adicionado(a) com sucesso!')
      except Exception as e:
        print(f'Erro ao exibir as autores(as)! - {e}')
        return
    
      input('Pressione uma tecla para continuar... ')

    def remove(self):
      print('\nRemovendo autor(a)...')
      try:
         id = int(input("Digite o ID para deletar do(a) autor(a): "))
         if self.__author_dao.delete(id):
            print('Autor(a) excluído(a) com sucesso')
         else:
            print('Autor(a) não encontrado.')
      except Exception as e:
        print(f'Erro ao deletar o(a) autor(a)! - {e}')
        return
    
      input('Pressione uma tecla para continuar... ')

    def showById(self):
       print('\nAutor(a) por ID...')
       try:
          id = int(input('Digite o ID do autor(a): '))
          author = self.__author_dao.getById(id)
          if author is not None:
             print(f'ID: {author.id} | Nome: {author.name.capitalize()} \nE-mail: {author.email} | Telefone: {showPhone(author.phone)}\nBio: {author.bio}')
          else:
             print('Autor(a) não encontrado.')
       except Exception as e:
        print(f'Erro ao exibir editora! - {e}')
        return   
    
       input('Pressione uma tecla para continuar...' )


    def showByName(self):
      print('\nAutor(a) por nome...')
      try:
         name = input('Digite o ID do autor(a): ').lower()
         author = self.__author_dao.getByName(name)
         if author is not None:
           print(f'ID: {author.id} | Nome: {author.name.capitalize()} \nE-mail: {author.email} | Telefone: {showPhone(author.phone)}\nBio: {author.bio}')
         else:
           print('Autor(a) não encontrado.')
      except Exception as e:
        print(f'Erro ao exibir editora! - {e}')
        return   
    
      input('Pressione uma tecla para continuar...' )

    def showByEmail(self):
      print('\nAutor(a) por e-mail...')
      try:
         email = input('Digite o ID do autor(a): ').lower()
         author = self.__author_dao.getByEmail(email)
         if author is not None:
           print(f'ID: {author.id} | Nome: {author.name.capitalize()} \nE-mail: {author.email} | Telefone: {showPhone(author.phone)}\nBio: {author.bio}')
         else:
           print('Autor(a) não encontrado.')
      except Exception as e:
        print(f'Erro ao exibir editora! - {e}')
        return   
    
      input('Pressione uma tecla para continuar...' )
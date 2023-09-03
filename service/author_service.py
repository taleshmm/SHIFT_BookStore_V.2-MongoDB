from dao.author_dao import AuthorDAO
from model.author import Author
from utils.util import showPhone, clearPhone
from utils.csv_processor import read_csv_author, create_csv_author
from utils.json_processor import read_json_author, create_json_author

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
     7 - Ler de arquivo CSV
     8 - Exportar para CSV
     9 - Ler de arquivo JSON
     10 - Exportar para JSON
     11 - Inserir arquivo no banco
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
        elif selection == '7':
           self.read_file('CSV')
        elif selection == '8':
           self.export_to_file('CSV')
        elif selection == '9':
           self.read_file('JSON')
        elif selection == '10':
           self.export_to_file('JSON')
        elif selection == '11':
           self.insert_many()
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
             print(f'{author.id} | {author.name.title()} | {author.email} | {showPhone(author.phone)} | {author.bio if author.bio != None else "Sem dados" }')
       except Exception as e:
         print(f'Erro ao exibir as autores(as)! - {e}')
         return
    
       input('Pressione uma tecla para continuar... ')

    def add(self):
      print('\nAdicionando autor(a)')
      try:
        name = input("Digite o nome: ").title()
        email = input("Digite o e-mail: ").lower()
        phone  = clearPhone(input("Digite o telefone: "))
        bio = input("Digite a bio: ")

        new_author = Author(name, email, phone, bio)
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
             print(f'ID: {author.id} | Nome: {author.name.title()} \nE-mail: {author.email} | Telefone: {showPhone(author.phone)}\nBio: {author.bio if author.bio != None else "Sem dados"}')
          else:
             print('Autor(a) não encontrado.')
       except Exception as e:
        print(f'Erro ao exibir editora! - {e}')
        return   
    
       input('Pressione uma tecla para continuar...' )

    def showByName(self):
      print('\nAutor(a) por nome...')
      try:
         name = input('Digite o ID do autor(a): ')
         author = self.__author_dao.getByName(name)
         if author is not None:
           print(f'ID: {author.id} | Nome: {author.name.title()} \nE-mail: {author.email} | Telefone: {showPhone(author.phone)}\nBio: {author.bio if author.bio != None else "Sem dados"}')
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
           print(f'ID: {author.id} | Nome: {author.name.title()} \nE-mail: {author.email} | Telefone: {showPhone(author.phone)}\nBio: {author.bio if author.bio != None else "Sem dados"}')
         else:
           print('Autor(a) não encontrado.')
      except Exception as e:
        print(f'Erro ao exibir editora! - {e}')
        return   
    
      input('Pressione uma tecla para continuar...' )
             
    def read_file(self, type_file: str):
      name_file = input(f'Digite o nome do arquivo {type_file} (Precisa estar na raiz do projeto). \n -> ')
      print(f'Listando do arquivo {type_file}...\n')
      try:
         authors = None
         if type_file == 'CSV':
            authors = read_csv_author(name_file)
         elif type_file == 'JSON':
            authors = read_json_author(name_file)
         else:
            print('O tipo de arquivo diferentes do suportado.')  
         for author in authors: 
           print(f'ID: {author.id} | Nome: {author.name.title()} \nE-mail: {author.email} | Telefone: {showPhone(author.phone)}\nBio: {author.bio if author.bio != None else "Sem dados"}')
      except Exception as e:
         print(f'Error ao exibir arquivo {type_file} - {e}')
            
    def export_to_file(self, type_file:str):
      name_file = input(f'Digite o nome do arquivo {type_file}: ')
      print(f'Criando arquivo {type_file}... \n')
      try:
         authors = self.__author_dao.getAll()
         if type_file == 'CSV':
            create_csv_author(name_file, authors)
         elif type_file == 'JSON':
            create_json_author(name_file, authors)
         else:
            print('O tipo de arquivo diferentes do suportado.')
      except Exception as e:
         print(f'Error ao criar arquivo {type_file} - {e}')
         
    def insert_many(self):
     try:
      type_file = input(' \nEscolha o tipo de arquivo:\n 1 - CSV\n 2 - JSON\n-> ')
      name_file = input('Digite o nome do arquivo: ')
      authors_file = None
      if type_file == '1':
        authors_file = read_csv_author(name_file)
      elif type_file == '2':
        authors_file = read_json_author(name_file)
      else: 
        print('Opção inválida, tente novamente!')
        return
      list_authors = list()
      print('Inserindo em banco...\n')
      for at in authors_file:
         list_authors.append((at.name, at.email, at.phone, at.bio))
      self.__author_dao.create_many(list_authors)
      print('Dados inseridos com sucesso.')
     except Exception as e:
       print(f'Error ao inserir dados no banco - {e}')
 
     

    
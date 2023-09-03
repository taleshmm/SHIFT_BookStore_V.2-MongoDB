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
     print('''\n[Categorias] Escolha uma das seguintes opções:
     1 - Listar todas as categorias
     2 - Adicionar nova categoria
     3 - Excluir categoria
     4 - Ver categoria por Id
     5 - Pesquisar categoria por nome
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
       print('Opção inválida! Por favor, tente novamente!')
     
     self.menu()

  def listAll(self):
    print('\nListando categorias...')

    try:
      categorys = self.__category_dao.getAll()
      if len(categorys) == 0:
        print('Nenhuma categoria encontrada!')
        
      for category in categorys:
        print(f'{category.id} | {category.name.title()}')
    except Exception as e:
      print(f'Erro ao exibir as categorias! - {e}')
      return
    
    input('Pressione uma tecla para continuar... ')

  def add(self):
    print('\nAdicionando categoria...')
    
    try:
      name = input('Digite o nome da categoria: ').title()
      new_category = Category(name)
      self.__category_dao.create(new_category)
      print('Categoria adicionada com sucesso!')
    except Exception as e:
      print(f'Erro ao inserir categoria! - {e}')
      return
    
    input('Pressione uma tecla para continuar... ')

  def remove(self):
    print('\nRemovendo categoria...')
    try:
      category_id = int(input('Digite o ID da categoria para excluir: '))
      if self.__category_dao.delete(category_id):
        print('Categoria excluída com sucesso!')
      else:
        print('Categoria não encontrada')
    except Exception as e:
      print(f'Error ao excluir a categoria! - {e}')
      return
    
    input('Pressione uma tecla para continuar... ')

  def showById(self):
    print('\nCategoria por Id...')
    
    try:
      id = int(input('Digite o ID da categoria: '))
      category = self.__category_dao.getById(id)
      if category is not None: 
        print(f'ID: {category.id} | Nome: {category.name.title()}')
      else:
        print('Categoria não encontrada')
    except Exception as e:
      print(f'Erro ao exibir categoria! - {e}')
      return   
    
    input('Pressione uma tecla para continuar...' )

  def showByName(self):
    print('\nCategoria por nome...')
    
    try:
      name = input('Digite o nome da categoria: ').title()
      category = self.__category_dao.getByName(name)
      if category is not None: 
        print(f'ID: {category.id} | Nome: {category.name.title()}')
      else:
        print('Categoria não encontrada')
    except Exception as e:
      print(f'Erro ao exibir categoria! - {e}')
      return   
    
    input('Pressione uma tecla para continuar... ')

  def read_file(self, type_file: str):
    name_file = input(f'Digite o nome do arquivo {type_file} (Precisa estar na raiz do projeto). \n -> ')
    print(f'Listando do arquivo {type_file}...\n')
    try:
      categories = None
      if type_file == 'CSV':
        categories = read_csv_category(name_file)
      elif type_file == 'JSON':
        categories = read_json_category(name_file)
      else:
        print('O tipo de arquivo diferentes do suportado.')  
      for cat in categories: 
         print(f'Nome: {cat.name.title()}')
    except Exception as e:
      print(f'Error ao exibir arquivo {type_file} - {e}')

  def export_to_file(self, type_file:str):
    name_file = input(f'Digite o nome do arquivo {type_file}: ')
    print(f'Criando arquivo {type_file}... \n')
    try:
      categories = self.__category_dao.getAll()
      if type_file == 'CSV':
        create_csv_category(name_file, categories)
      elif type_file == 'JSON':
        create_json_category(name_file, categories)
      else:
         print('O tipo de arquivo diferentes do suportado.')
    except Exception as e:
      print(f'Error ao criar arquivo {type_file} - {e}')
      
  def insert_many(self):
     try:
      type_file = input(' \nEscolha o tipo de arquivo:\n 1 - CSV\n 2 - JSON\n-> ')
      name_file = input('Digite o nome do arquivo: ')
      categories_file = None
      if type_file == '1':
        categories_file = read_csv_category(name_file)
      elif type_file == '2':
        categories_file = read_json_category(name_file)
      else: 
        print('Opção inválida, tente novamente!')
        return
      list_categories = list()
      print('\n Inserindo em banco...\n')
      for cat in categories_file:
        list_categories.append((cat.name,))
      self.__category_dao.create_many(list_categories)
      print('Dados inseridos com sucesso.')
     except Exception as e:
       print(f'Error ao inserir dados no banco - {e}')
       
      
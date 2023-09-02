from dao.category_dao import CategoryDAO
from model.category import Category
from utils.csv_processor import read_csv_category, create_csv_category

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
     8 - Inserir CSV no banco
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
       self.read_csv()
     elif selection == '7':
       self.create_csv()
     elif selection == '8':
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

  def read_csv(self):
    name_file = input('Digite o nome do arquivo CSV (Precisa estar na raiz do projeto). \n -> ')
    print('Listando do arquivo CSV...\n')
    try:
      categories = read_csv_category(name_file)
      for cat in categories: 
         print(f'Nome: {cat.name.title()}')
    except Exception as e:
      print(f'Error ao exibir arquivo CSV - {e}')

  def create_csv(self):
    name_file = input('Digite o nome do arquivo CSV: ')
    print('Criando arquivo CSV... \n')
    try:
      categories = self.__category_dao.getAll()
      create_csv_category(name_file, categories)
    except Exception as e:
      print(f'Error ao criar arquivo CSV - {e}')
      
  def insert_many(self):
     try:
      name_file = input('Digite o nome do arquivo CSV: ')
      categories_csv = read_csv_category(name_file)
      list_categories = list()
      print('Inserindo em banco...\n')
      for cat in categories_csv:
        list_categories.append((cat.name,))
      self.__category_dao.create_many(list_categories)
      print('Dados inseridos com sucesso.')
     except Exception as e:
       print(f'Error ao inserir dados no banco - {e}')
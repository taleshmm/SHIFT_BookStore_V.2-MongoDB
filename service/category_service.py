from dao.category_dao import CategoryDAO
from model.category import Category

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
        print(f'{category.id} | {category.name.capitalize()}')
    except Exception as e:
      print(f'Erro ao exibir as categorias! - {e}')
      return
    
    input('Pressione uma tecla para continuar... ')

  def add(self):
    print('\nAdicionando categoria...')
    
    try:
      id = self.__category_dao.getLastId() + 1
      name = input('Digite o nome da categoria: ').lower()
      new_category = Category(id, name)
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
        print(f'ID: {category.id} | Nome: {category.name.capitalize()}')
      else:
        print('Categoria não encontrada')
    except Exception as e:
      print(f'Erro ao exibir categoria! - {e}')
      return   
    
    input('Pressione uma tecla para continuar...' )

  def showByName(self):
    print('\nCategoria por nome...')
    
    try:
      name = input('Digite o nome da categoria: ').lower()
      category = self.__category_dao.getByName(name)
      if category is not None: 
        print(f'ID: {category.id} | Nome: {category.name.capitalize()}')
      else:
        print('Categoria não encontrada')
    except Exception as e:
      print(f'Erro ao exibir categoria! - {e}')
      return   
    
    input('Pressione uma tecla para continuar... ')



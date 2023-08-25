from dao.editor_dao import EditorDAO
from model.editor import Editor
from utils.util import showPhone, clearPhone

class EditorService:
    def __init__(self):
      self.__editor_dao = EditorDAO()
    
    @property
    def editor_dao(self) -> EditorDAO:
       return self.__editor_dao
    
    def menu(self):
        print('''\n[Editoras] Escolha uma das seguintes opções:
     1 - Listar todas as editoras
     2 - Adicionar nova editora
     3 - Excluir editora
     4 - Ver editora por Id
     5 - Pesquisar editora por nome
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
      print('\nListando editoras...')
      try:
         editors = self.__editor_dao.getAll()
         if len(editors) == 0:
            print('Nenhuma editora encontrada!')
         else:
          print('ID | Nome  | Telefone |   Endereço')
          for editor in editors:
              print(f'{editor.id} | {editor.name.capitalize()} | {showPhone(editor.phone)} | {editor.address.capitalize()}')
      except Exception as e:
        print(f'Erro ao exibir as editoras! - {e}')
        return
    
      input('Pressione uma tecla para continuar... ')
   
    def add(self):
       print('\nAdicionando editora...')
       try:
          id = self.__editor_dao.getLastId() + 1
          name = input('Digite o nome da editora: ').lower()
          phone = input('Digite o telefone: ')
          address = input('Digite o endereço: ').lower()

          new_editor = Editor(id, name, address, clearPhone(phone))
          self.__editor_dao.create(new_editor)
          print('Editora adicionada com sucesso!')
       except Exception as e:
        print(f'Erro ao inserir editora! - {e}')
        return
    
       input('Pressione uma tecla para continuar... ')
       
    def remove(self):
        print('\Removendo editora...')
        try:
           id = int(input('Digite o ID da editora que deseja deletar: '))
           if self.__editor_dao.delete(id):
              print('Editora excluída com sucesso!')
           else:
              print('Editora não encontrada')
        except Exception as e:
          print(f'Erro ao deletar editora! - {e}')
          return
    
        input('Pressione uma tecla para continuar... ')

    def showById(self):
       print('\Editora por Id...')

       try:
          id = int(input('Digite o ID da editora: '))
          editor = self.__editor_dao.getById(id)
          if editor is not None:
             print(f'ID: {editor.id} | Nome: {editor.name.capitalize()} | {showPhone(editor.phone)}')
          else:
             print('Editora não encontrada! ')
       except Exception as e:
          print(f'Erro ao exibir editora! - {e}')
          return   
    
       input('Pressione uma tecla para continuar...' )

    def showByName(self):
      print('\Editora por nome...')
    
      try:
        name = input('Digite o nome da editora: ').lower()
        editor = self.__editor_dao.getByName(name)
        if editor is not None: 
           print(f'ID: {editor.id} | Nome: {editor.name.capitalize()} | {showPhone(editor.phone)}')
        else:
          print('Editora não encontrada!')
      except Exception as e:
        print(f'Erro ao exibir editora! - {e}')
        return   
      
      input('Pressione uma tecla para continuar... ')



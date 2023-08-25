from model.editor import Editor

class EditorDAO:
    def __init__(self):
        self.__editors: list[Editor] = list()
    
    def getAll(self) -> list[Editor]:
        return self.__editors
    
    def create(self, editor: Editor) -> None:
        self.__editors.append(editor)
    
    def delete(self, editor_id: int) -> bool:
        find = False
        for i in self.__editors:
          if editor_id == i.id:
            index = self.__editors.index(i)
            del self.__editors[index]
            find = True
            break
        return find
    
    def getById(self, editor_id: id) -> Editor:
       find_editor = None
       for i in self.__editors:
         if i.id == editor_id:
            find_editor = i
            break
       return find_editor
    
    def getLastId(self) -> int:
       if len(self.__editors) != 0:
          return self.__editors[-1].id
       else:
          return 0
    
    def getByName(self, editor_name: str) -> Editor:
       find_editor = None
       for i in self.__editors:
          if i.name == editor_name:
             find_editor = i
             break
       return find_editor
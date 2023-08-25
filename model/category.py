class Category:
    def __init__(self, id: int, name: str):
        self.__id: int = id
        self.__name: str = name

    @property
    def id(self) -> int:
        return self.__id
    
    @id.setter
    def id(self, id: int):
      self.__id = id

    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name: str):
        self.__name = name
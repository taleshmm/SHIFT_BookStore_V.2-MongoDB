class Editor:
    def __init__(self, id: int, name: str, address: str, phone: str):
        self.__id: int = id
        self.__name: str = name
        self.__address: str = address
        self.__phone: str = phone

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
    
    @property
    def address(self) -> str:
      return self.__address
      
    @address.setter
    def address(self, address: str):
      self.__address = address

    @property
    def phone(self) -> str:
      return self.__phone
    
    @phone.setter
    def phone(self, phone: str):
      self.__phone = phone
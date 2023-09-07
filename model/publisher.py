from bson import ObjectId

class Publisher:
    def __init__(self, name: str, address: str, phone: str):
        self.__id: ObjectId = None
        self.__name: str = name
        self.__address: str = address
        self.__phone: str = phone

    @property
    def id(self) -> ObjectId:
      return self.__id
    
    @id.setter
    def id(self, id: ObjectId):
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
    
    def in_dump(self) -> dict:
      return {'name': self.__name, 'address': self.__address, 'phone': self.__phone}
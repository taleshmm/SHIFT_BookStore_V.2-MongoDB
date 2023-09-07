from bson import ObjectId

class Category:
    def __init__(self, name: str):
        self.__id: ObjectId = None
        self.__name: str = name

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
    
    def in_dump(self) -> dict:
        return {'name': self.__name}
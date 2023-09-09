from bson import ObjectId

class Author:
    def __init__(self, name: str, email: str, phone: str, bio: str):
        self.__id: ObjectId = None
        self.__name: str = name
        self.__email: str = email
        self.__phone: str = phone
        self.__bio: str = bio

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
    def email(self) -> str:
       return self.__email
    
    @email.setter
    def email(self, email: str):
       self.__email = email
    
    @property
    def phone(self) -> str:
      return self.__phone
    
    @phone.setter
    def phone(self, phone: str):
       self.__phone = phone
    
    @property
    def bio(self) -> str:
      return self.__bio
    
    @bio.setter
    def bio(self, bio: str):
       self.__bio = bio
    
    def in_dump(self) -> dict:
      return {'name': self.__name, 'email': self.__email, 'phone': self.__phone, 'bio': self.__bio}
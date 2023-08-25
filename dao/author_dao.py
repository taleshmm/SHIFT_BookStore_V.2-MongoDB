from model.author import Author

class AuthorDAO:
  def __init__ (self):
      self.__authors: list[Author] = list()
  
  def getAll(self) ->  list[Author]:
     return self.__authors
  
  def create(self, author: Author) -> None:
     self.__authors.append(author)

  def delete(self, author_id) -> bool:
     find = False
     for i in self.__authors:
        if i.id == author_id:
          index = self.__authors.index(i)
          del self.__authors[index]
          find = True
          break
     return find
  
  def getById(self, author_id) -> Author:
     find_author = None
     for i in self.__authors:
        if i.id == author_id:
           find_author = i
           break
     return find_author

  def getLastId(self) -> int:
    if len(self.__authors) != 0:
      return self.__authors[-1].id
    else:
      return 0
  
  def getByName(self, author_name: str) -> Author:
       find_author = None
       for i in self.__authors:
          if i.name == author_name:
             find_author = i
             break
       return find_author
  
  def getByEmail(self, author_email: str) -> Author:
       find_author = None
       for i in self.__authors:
          if i.email == author_email:
             find_author = i
             break
       return find_author
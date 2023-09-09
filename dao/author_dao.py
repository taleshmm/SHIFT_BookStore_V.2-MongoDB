from model.author import Author
from database.client_factory import ClientFactory
from bson import ObjectId

class AuthorDAO:
  def __init__ (self):
      self.__client_factory = ClientFactory()
  
  def getAll(self) ->  list[Author]:
     authors = list()
     client = self.__client_factory.get_client()
     db = client.bookStore
     for doc in db.authors.find():
        aut = Author(doc.get('name', 'No data'), doc.get('email', 'No data'), doc.get('phone', 'No data'), doc.get('bio', 'No data'))
        aut.id = doc['_id']
        authors.append(aut) 
     client.close()
     return authors
        
  
  def create(self, author: Author) -> None:
     client = self.__client_factory.get_client()
     db = client.bookStore
     db.authors.insert_one({'name': author.name, 'email': author.email, 'phone': author.phone, 'bio': author.bio})
     client.close()

  def delete(self, author_id) -> bool:
     client = self.__client_factory.get_client()
     db = client.bookStore
     result = db.authors.delete_one({'_id': ObjectId(author_id)})
     client.close()
     if result.deleted_count == 1:
        return True
     return False
  
  def getById(self, author_id) -> Author:
     client = self.__client_factory.get_client()
     db = client.bookStore
     result = db.authors.find_one({'_id': ObjectId(author_id)})
     find_author = None
     client.close()
     if result:
        find_author = Author(result.get('name', 'No data'), result.get('email', 'No data'), result.get('phone', 'No data'), result.get('bio', 'No data'))
     return find_author
     
  def getByName(self, author_name: str) -> Author:
     client = self.__client_factory.get_client()
     db = client.bookStore
     result = db.authors.find_one({'name': author_name})
     find_author = None
     client.close()
     if result:
        find_author = Author(result.get('name', 'No data'), result.get('email', 'No data'), result.get('phone', 'No data'), result.get('bio', 'No data'))
     return find_author
  
  def getByEmail(self, author_email: str) -> Author:
     client = self.__client_factory.get_client()
     db = client.bookStore
     result = db.authors.find_one({'email': author_email})
     find_author = None
     client.close()
     if result:
        find_author = Author(result.get('name', 'No data'), result.get('email', 'No data'), result.get('phone', 'No data'), result.get('bio', 'No data'))
     return find_author
  
  def create_many(self, authors):
        client = self.__client_factory.get_client()
        db = client.bookStore
        db.authors.insert_many(authors)
        client.close()
from model.author import Author
from database.client_factory import ClientFactory

class AuthorDAO:
  def __init__ (self):
      self.__connection_factory = ClientFactory()
  
  def getAll(self) ->  list[Author]:
     connect = self.__connection_factory.get_connection()
     cursor = connect.cursor()
     cursor.execute('SELECT * FROM authors')
     rows = cursor.fetchall()
     cursor.close()
     connect.close()
     authors = list()
     for row in rows:
        authorRow = Author(row[1], row[2], row[3], row[4], row[0])
        authors.append(authorRow)
     
     return authors
        
  
  def create(self, author: Author) -> None:
     connect = self.__connection_factory.get_connection()
     cursor = connect.cursor()
     cursor.execute("INSERT INTO authors (name, email, phone, bio) VALUES (%s, %s, %s, %s)", (author.name, author.email, author.phone, author.bio))
     connect.commit()
     cursor.close()
     connect.close()

  def delete(self, author_id) -> bool:
     connect = self.__connection_factory.get_connection()
     cursor = connect.cursor()
     cursor.execute("DELETE FROM authors WHERE id = %s", (author_id,))
     rows_deleted = cursor.rowcount
     connect.commit()
     cursor.close()
     connect.close()
     if rows_deleted > 0:
        return True
     return False
  
  def getById(self, author_id) -> Author:
     connect = self.__connection_factory.get_connection()
     cursor = connect.cursor()
     cursor.execute("SELECT * FROM authors WHERE id = %s", (author_id,))
     row = cursor.fetchone()
     cursor.close()
     cursor.close()
     find_author = None
     if row:
        find_author = Author(row[1], row[2], row[3], row[4], row[0])
     return find_author
     
  def getByName(self, author_name: str) -> Author:
     connect = self.__connection_factory.get_connection()
     cursor = connect.cursor()
     cursor.execute("SELECT * FROM authors WHERE name = %s", (author_name,))
     row = cursor.fetchone()
     cursor.close()
     cursor.close()
     find_author = None
     if row:
        find_author = Author(row[1], row[2], row[3], row[4], row[0])
     return find_author
  
  def getByEmail(self, author_email: str) -> Author:
     connect = self.__connection_factory.get_connection()
     cursor = connect.cursor()
     cursor.execute("SELECT * FROM authors WHERE email = %s", (author_email,))
     row = cursor.fetchone()
     cursor.close()
     cursor.close()
     find_author = None
     if row:
        find_author = Author(row[1], row[2], row[3], row[4], row[0])
     return find_author
  
  def create_many(self, authors):
        connect = self.__connection_factory.get_connection()
        cursor = connect.cursor()
        cursor.executemany("INSERT INTO authors (name, email, phone, bio) VALUES (%s, %s, %s, %s)", authors)
        connect.commit()
        cursor.close()
        connect.close()
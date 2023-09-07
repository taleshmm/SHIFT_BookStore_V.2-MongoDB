from model.publisher import Publisher
from database.client_factory import ClientFactory

class PublisherDAO:
    def __init__(self):
        self.__connection_factory = ClientFactory()
    
    def getAll(self) -> list[Publisher]:
        connect = self.__connection_factory.get_connection()
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM publishers")
        rows = cursor.fetchall()
        publishers = list()
        for row in rows:
            publisherRow = Publisher(row[1], row[2], row[3], row[0])
            publishers.append(publisherRow)
        cursor.close()
        connect.close()
        return publishers
    
    def create(self, publisher: Publisher) -> None:
        connect = self.__connection_factory.get_connection()
        cursor = connect.cursor()
        cursor.execute("INSERT INTO publishers (name, address, phone) VALUES (%s, %s, %s)", (publisher.name, publisher.address, publisher.phone))
        connect.commit()
        cursor.close()
        connect.close()
        

    def delete(self, publisher_id: int) -> bool:
        connect = self.__connection_factory.get_connection()
        cursor = connect.cursor()
        cursor.execute("DELETE FROM publishers WHERE id = %s", (publisher_id,))
        rows_deleted = cursor.rowcount
        connect.commit()
        cursor.close()
        connect.close()
        if rows_deleted > 0:
            return True
        return False

    def getById(self, publisher_id: id) -> Publisher:
       connect = self.__connection_factory.get_connection()
       cursor = connect.cursor()
       cursor.execute("SELECT * FROM publishers WHERE id = %s", (publisher_id,))
       row = cursor.fetchone()
       cursor.close()
       connect.close()
       find_publisher = None
       if row:
           find_publisher = Publisher(row[1], row[2], row[3], row[0])
       return find_publisher     
    
    def getByName(self, publisher_name: str) -> Publisher:
        connect = self.__connection_factory.get_connection()
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM publishers WHERE name = %s", (publisher_name,))
        row = cursor.fetchone()
        cursor.close()
        connect.close()
        find_publisher = None
        if row:
           find_publisher = Publisher(row[1], row[2], row[3], row[0])
        return find_publisher   
    
    def create_many(self, publishers):
        connect = self.__connection_factory.get_connection()
        cursor = connect.cursor()
        cursor.executemany("INSERT INTO publishers (name, address, phone) VALUES (%s, %s, %s)", publishers)
        connect.commit()
        cursor.close()
        connect.close()
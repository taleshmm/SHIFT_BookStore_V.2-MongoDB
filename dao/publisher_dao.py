from model.publisher import Publisher
from database.client_factory import ClientFactory
from bson import ObjectId

class PublisherDAO:
    def __init__(self):
        self.__client_factory = ClientFactory()
    
    def getAll(self) -> list[Publisher]:
        publishers = list()
        client = self.__client_factory.get_client()
        db = client.bookStore
        for doc in db.publishers.find():
            pub = Publisher(doc.get('name', 'No data'), doc.get('address', 'No data'), doc.get('phone', 'No data'))  
            pub.id = doc['_id'] 
            publishers.append(pub)
        client.close()     
        return publishers
   
    
    def create(self, publisher: Publisher) -> None:
        client = self.__client_factory.get_client()
        db = client.bookStore
        db.publishers.insert_one({'name': publisher.name, 'address': publisher.address, 'phone': publisher.phone})
        client.close()
        

    def delete(self, publisher_id: int) -> bool:
        client = self.__client_factory.get_client()
        db = client.bookStore
        result = db.publishers.delete_one({'_id': ObjectId(publisher_id)})
        client.close()     
        if result.deleted_count == 1:
            return True
        return False

    def getById(self, publisher_id: id) -> Publisher:
       find_publisher = None
       client = self.__client_factory.get_client()
       db = client.bookStore
       result = db.publishers.find_one({'_id': ObjectId(publisher_id)})
       client.close()
       if result:
           find_publisher = Publisher(result.get('name', 'No data'), result.get('address', 'No data'), result.get('phone', 'No data'))
           find_publisher.id = result['_id']
       return find_publisher     
    
    def getByName(self, publisher_name: str) -> Publisher:
       find_publisher = None
       client = self.__client_factory.get_client()
       db = client.bookStore
       result = db.publishers.find_one({'name': publisher_name})
       client.close()
       if result:
           find_publisher = Publisher(result.get('name', 'No data'), result.get('address', 'No data'), result.get('phone', 'No data'))
           find_publisher.id = result['_id']
       return find_publisher     
    
    def create_many(self, publishers):
        client = self.__client_factory.get_client()
        db = client.bookStore
        db.publishers.insert_many(publishers)
        client.close()
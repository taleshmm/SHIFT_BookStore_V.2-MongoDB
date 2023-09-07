from model.category import Category
from database.client_factory import ClientFactory
from bson import ObjectId

class CategoryDAO:
    def __init__(self): 
        self.__client_factory = ClientFactory() 

    def getAll(self) -> list[Category]:
        categories = list()
        client = self.__client_factory.get_client()
        db =client.bookStore
        for doc in db.category.find():
            cat = Category(doc['name'])
            cat.id = doc['_id']
            categories.append(cat)
        client.close()
        return categories
    
    def create(self, category: Category) -> None:
        client = self.__client_factory.get_client()
        db = client.bookStore
        db.category.insert_one({'name': category.name})
        client.close()

    def delete(self, category_id: int) -> bool:
        client = self.__client_factory.get_client()
        db = client.bookStore
        result = db.category.delete_one({'_id': ObjectId(category_id)})
        client.close()
        if result.deleted_count == 1:
            return True       
        return False
    
    def getById(self, category_id: int) -> Category:
        find_category = None
        client = self.__client_factory.get_client()
        db = client.bookStore
        result = db.category.find_one({'_id': ObjectId(category_id)})
        client.close()
        if result:
            find_category = Category(result['name'])
            find_category.id = result['_id']
        return find_category

    def getByName(self, category_name: str) -> Category:
       find_category = None
       client = self.__client_factory.get_client()
       db = client.bookStore
       result = db.category.find_one({'name': category_name})
       client.close()
       if result:
        find_category = Category(result['name'])
        find_category.id = result['_id']
       return find_category
    
    def create_many(self, categories):
        client = self.__client_factory.get_client()
        db = client.bookStore
        db.category.insert_many(categories)
        client.close()
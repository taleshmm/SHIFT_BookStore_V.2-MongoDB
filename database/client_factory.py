from pymongo import MongoClient
from pymongo.server_api import ServerApi

    
class ClientFactory:
    def get_client(self):
        '''MongoDB Connection using MongoClient.

    This function establishes a connection to a MongoDB server using the MongoClient from pymongo. You need to provide a valid MongoDB connection URL.

    Parameters:
        - connection_url (str): The MongoDB connection URL.
        - server_api (ServerApi): Optional. The MongoDB Server API version (e.g., ServerApi('1')). Default is None.

    Returns:
        - client: The MongoDB client instance connected to the specified database.

    Example Usage:
        client = MongoClient('mongodb+srv://username:password@cluster.mongodb.net/', server_api=ServerApi('1'))
        db = client.get_database('your_database_name')
        collection = db.get_collection('your_collection_name')
        document = {"key": "value"}
        collection.insert_one(document)
        client.close()

    Please make sure to replace 'username', 'password', 'cluster.mongodb.net', 'your_database_name', and 'your_collection_name' with your actual MongoDB connection details.
'''    
        return MongoClient('your_database', server_api=ServerApi('1'))
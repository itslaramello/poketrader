import pymongo
import os

class MongoConnection(object):
    db_host: str
    db_port: int
    db_user: str
    db_password: str
    db_name: str

    def __init__(self):
        self.db_host = os.getenv('DB_HOST','localhost')
        self.db_port = int(os.getenv('DB_PORT',27017))
        self.db_user = os.getenv('DB_USER',"")
        self.db_password = os.getenv('DB_PASSWORD',"")
        self.db_name = 'poke-trader'

    def connect(self,collection):
        connection = pymongo.MongoClient(host=self.db_host, port=self.db_port, username=self.db_user, password=self.db_password,authSource=self.db_name)
        db = connection.get_database(self.db_name)
        collection = db[collection]
        return collection
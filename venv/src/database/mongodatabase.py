from database.database import Database
from pymongo import MongoClient

class Mongodatabase(Database):

    db = None

    def __init__(self, config):
        client = MongoClient(config['url'], config['port'])
        self.db = client[config['table']]

    def insertvalue(self, value):
        self.db.sadface.insert_one(value)
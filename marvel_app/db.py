import configparser
from pymongo import MongoClient
from configparser import ConfigParser

from pprint import pprint

class MongoDB:
    def __init__(self, config_file) -> None:
        self._config = ConfigParser()
        self._config.read(config_file)
        self._mongo_url = self._config['db']['connection_string']
    
 
    def get_mongo_client(self):
        self.client = MongoClient(self._mongo_url)
        return self.client




if __name__ == '__main__':
    mongo = MongoDB('config/account.ini')
    client = mongo.get_mongo_client()
    db = client.admin
    serverStatusResult = db.command("serverStatus")
    pprint(serverStatusResult)



import pymongo
import os
from configparser import ConfigParser

db_conf = ConfigParser()
db_conf.read(os.path.join(os.getcwd(),'config.ini'))

def create_mongo_client():
    return pymongo.MongoClient(db_conf['db']['mongo_url'])
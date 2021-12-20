# web/__init__.py
from flask import Flask
from flask_bootstrap import Bootstrap
import pymongo
import os
from configparser import ConfigParser


def get_db_uri():
   config = ConfigParser()
   config.read(os.path.join(os.getcwd(),'web','api_consumer','config.ini')) 
   return config['db']['mongo_url']

db = pymongo.MongoClient(get_db_uri())

bootstrap = Bootstrap()

def create_app(config_type):
    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(),"web","config", f"{config_type}.py")
    app.config.from_pyfile(configuration)
    
    bootstrap.init_app(app)

    from web.characters import characters
    app.register_blueprint(characters)

    return app
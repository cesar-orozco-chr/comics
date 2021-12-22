from configparser import ConfigParser
from hashlib import md5
from time import time
import requests
import os
from .backend import create_mongo_client

class BaseEndpoint():

    def __init__(self, 
                endpoint_index,
                config_file=os.path.join(os.getcwd(),'config.ini') ) -> None:
        self._config = ConfigParser()
        self._config.read(config_file)
        self._private_key = self._config['api']['private_key']
        self._public_key = self._config['api']['public_key']
        self.base_endpoint = self._config['endpoint'][endpoint_index]
    
    def payload(self):
        ts = int(time())
        input_string = str(ts) + self._private_key + self._public_key
        hash = md5(input_string.encode('utf-8')).hexdigest()
        return {
            'ts':ts,
            'apikey': self._public_key,
            'hash': hash
        }
    def get_base_endpoint(self):
        return self.base_endpoint


class CharactersEndpoint(BaseEndpoint):

    def __init__(self, endpoint_index ='characters', config_file=os.path.join(os.getcwd(), 'config.ini')) -> None:
        super().__init__(endpoint_index, config_file=config_file)

class ComicsEndpoint(BaseEndpoint):

    def __init__(self, endpoint_index='comics', config_file=os.path.join(os.getcwd(), 'config.ini')) -> None:
        super().__init__(endpoint_index, config_file=config_file)

class BaseRequest():

    def __init__(self) -> None:
        pass

    def get_results(self, endpoint, params):
        json_response = requests.get(endpoint, params=params).json()
        return json_response['data']['results']


if __name__ == '__main__':
    endpoint = CharactersEndpoint()
    print(dir(endpoint))
    print(endpoint.payload())
    character_endpoint = endpoint.get_base_endpoint()
    r = BaseRequest().get_results(character_endpoint,endpoint.payload())
    
    client = create_mongo_client()
    db = client.marvel_raw

    result = db.characters.insert_many(r)
    print(f"Inserted {result.inserted_ids}")

from marvel import Marvel
from db import MongoDB
from configparser import ConfigParser
import json
import os

marvel_creds = ConfigParser()

marvel_creds.read('config/account.ini')

PUBLIC_KEY = marvel_creds['marvel account']['public_key']
PRIVATE_KEY = marvel_creds['marvel account']['private_key'] 

m = Marvel(PUBLIC_KEY, PRIVATE_KEY)

def write_json_sample(data, json_file):
    with open(json_file, 'w') as f:
        f.write(json.dumps(data))

def read_json_sample(json_file):
    with open(json_file, 'r') as f:
        results = json.load(f)
    return results

def query_character():
    characters = m.characters.get(1011334)

    print(characters, type(characters))

    write_json_sample(data=characters, json_file='character.json')
    

def query_comics():
    comics = m.comics.get(21366)

    write_json_sample(data=comics, json_file='comics.json')

def query_creators():
    creators = m.creators.get(2133)
    write_json_sample(data=creators, json_file='creator.json')

def query_events():
    event = m.events.get(269)
    write_json_sample(event, 'event.json')

def query_series():
    serie = m.series.get(1945)
    write_json_sample(serie, 'serie.json')

def query_stories():
    story = m.stories.get(47184)
    write_json_sample(story, 'story.json')
    
def describe_dict(data):
    result = []
    for k,v in data.items():
        result.append([k,type(v)])
    return result

if __name__ == '__main__':
    with open('marvel_schema.txt', 'w') as fw:   

        for f in ['event.json', 
                'serie.json', 
                'story.json',
                'character.json',
                'comics.json',
                'creator.json']:
            fw.write(f.split('.')[0]+'\n')
            if not os.path.exists(f):
                if 'character' in f:
                    query_character()
                elif 'serie' in f:
                    query_series()
                elif 'event' in f:
                    query_events()
                elif 'comics' in f:
                    query_comics()
                elif 'creator' in f:
                    query_creators()
                elif 'story' in f:
                    query_stories()
            fw.write(str(
                describe_dict(read_json_sample(f)['data']['results'][0])
                )+'\n')
    # insert a character in db
    mongo_client = MongoDB('config/account.ini').get_mongo_client()
    characters = mongo_client.marvel.characters
    c = read_json_sample('character.json')['data']['results'][0]
    result = characters.insert_one(c)
    print('Inserted {0} on collection'.format(result.inserted_id))  

    """
    TO DO
    1. Validate inserted data in a collection
    2. Query all characters and store in Mongo db
    3. Query all comics associated to each character and store in Mongo db
    """      


        
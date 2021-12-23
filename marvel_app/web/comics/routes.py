# web/comics/routes.py
from web import db
from flask import render_template, flash, jsonify
from web.comics import comics
from web.api_consumer.requester import ComicsEndpoint, BaseRequest
from web.resources.util import add_id, get_id_from_url
import os


collection = db.marvel.comics
CONFIG_FILE = os.path.join(os.getcwd(),'web','api_consumer','config.ini')

def get_details_from_comic(obj):
    serie = obj['series']
    serie['id'] = get_id_from_url(serie['resourceURI'])
    characters = add_id(obj['characters']['items'],'resourceURI',"")
    stories = add_id(obj['stories']['items'],'resourceURI','')
    creators = add_id(obj['creators']['items'],'resourceURI','')
    return (serie, characters, stories, creators)

@comics.route('/comics/<id>')
def display_comic_by_id(id):
    endpoint = ComicsEndpoint(config_file=CONFIG_FILE)
    params = endpoint.payload()
    respose = BaseRequest().get_results(
        endpoint.get_base_endpoint()+'/'+str(id),
        params
    )
    comic = respose[0]
    serie, characters, stories, creators = get_details_from_comic(comic)
    return render_template('comic_details.html',comic=comic, 
                            serie=serie,
                            stories=stories,
                            characters=characters,
                            creators=creators        
                        )



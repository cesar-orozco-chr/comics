# web/comics/routes.py
from web import db
from flask import render_template, flash, jsonify
from web.comics import comics
from web.api_consumer.requester import ComicsEndpoint, BaseRequest
from web.resources.util import add_id
import os


collection = db.marvel.comics
CONFIG_FILE = os.path.join(os.getcwd(),'web','api_consumer','config.ini')

@comics.route('/comics/<id>')
def display_comic_by_id(id):
    endpoint = ComicsEndpoint(config_file=CONFIG_FILE)
    params = endpoint.payload()
    respose = BaseRequest().get_results(
        endpoint.get_base_endpoint()+'/'+str(id),
        params
    )
    comic = respose[0]
    serie = comic['series']
    characters = add_id(comic['characters']['items'],'resourceURI',"url_for('/')")
    stories = comic['stories']['items']
    return render_template('comic_details.html',comic=comic, 
                            serie=serie,
                            stories=stories,
                            characters=characters)



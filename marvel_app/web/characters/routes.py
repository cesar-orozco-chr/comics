from web import db
from flask import render_template, flash, redirect, url_for
from web.characters import characters
from web.api_consumer.requester import CharactersEndpoint, BaseRequest
from web.resources.util import add_id
import os

collection = db.marvel_raw.characters
CONFIG_FILE = os.path.join(os.getcwd(),'web','api_consumer','config.ini')

def get_details_from_character(obj):
    return  (add_id(obj['comics']['items'],'resourceURI'), 
            add_id(obj['series']['items'],'resourceURI'), 
            add_id(obj['stories']['items'],'resourceURI'), 
            add_id(obj['events']['items'],'resourceURI'))


@characters.route('/')
def display_characters():
    character_list = collection.find()
    return render_template('home.html', characters=character_list)


@characters.route('/character/details/<char_name>')
def character_details(char_name):
    c = collection.find_one({'name':char_name})
    comics, series, stories, events = get_details_from_character(c)
    return render_template('details.html', c=c, 
                            comics=comics,
                            series=series,
                            stories=stories,
                            events=events)

@characters.route('/character/<id>')
def character_details_by_id(id):
    endpoint = CharactersEndpoint(config_file=CONFIG_FILE)
    params = endpoint.payload()
    respose = BaseRequest().get_results(
        endpoint.get_base_endpoint()+'/'+str(id),
        params
    )
    c = respose[0]
    comics, series, stories,events = get_details_from_character(c)
    return render_template('details.html', c=c, 
                            comics=comics,
                            series=series,
                            stories=stories,
                            events=events)

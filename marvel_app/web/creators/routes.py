# web/creators/routes.py
from web import db
from flask import render_template
from web.creators import creators
from web.resources.util import add_id
from web.api_consumer.requester import CreatorsEndpoint, BaseRequest
import os

collection = db.marvel.creators
CONFIG_FILE = os.path.join(os.getcwd(),'web','api_consumer','config.ini')

def get_details_from_creator(obj):
    comics = add_id(obj['comics']['items'],'resourceURI')
    series = add_id(obj['series']['items'],'resourceURI')
    return (comics, series)

@creators.route('/creators/<id>')
def display_creators_by_id(id):
    endpoint = CreatorsEndpoint(config_file=CONFIG_FILE)
    params = endpoint.payload()
    print(endpoint.get_base_endpoint())
    response = BaseRequest().get_results(
        endpoint.get_base_endpoint() +'/'+str(id),
        params
    )
    creator = response[0]
    comics, series = get_details_from_creator(creator)
    return render_template('creator_detail.html',
                            creator=creator,
                            comics=comics,
                            series=series
                           )

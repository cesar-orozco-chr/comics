# web/characters/__init__.py
from flask import Blueprint

characters = Blueprint('characters', __name__, template_folder='templates')

from web.characters import routes
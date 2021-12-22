# web/comics/__init__.py
from flask import Blueprint

comics = Blueprint('comics', __name__, template_folder='templates')

from web.comics import routes
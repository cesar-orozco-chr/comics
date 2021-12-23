# web/creators/__init__.py
from flask import Blueprint

creators = Blueprint('creators', __name__, template_folder='templates')

from web.creators import routes
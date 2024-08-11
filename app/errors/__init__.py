from flask import blueprints, Blueprint

bp = Blueprint('errors', __name__)

from app.errors import handlers
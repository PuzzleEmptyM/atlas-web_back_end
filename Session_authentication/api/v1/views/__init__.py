# api/v1/views/__init__.py
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Importing all other views here...
from api.v1.views.index import *
from api.v1.views.users import *
from api.v1.views.session_auth import *

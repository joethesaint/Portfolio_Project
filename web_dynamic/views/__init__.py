from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix="/")
from web_dynamic.views.homepage import *
from web_dynamic.views.user import *
from web_dynamic.views.view import *
from web_dynamic.views.admin import *

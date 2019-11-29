# app/admin/__init__.py

from flask import Blueprint

loader = Blueprint('loader', __name__)




from . import views
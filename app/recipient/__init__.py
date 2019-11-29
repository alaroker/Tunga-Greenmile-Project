# app/admin/__init__.py

from flask import Blueprint

recipient = Blueprint('recipient', __name__)




from . import views
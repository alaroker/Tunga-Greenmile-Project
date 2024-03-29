# app/__init__.py

# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap


# local imports
from config import app_config

# db variable initialization
login_manager = LoginManager()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    
    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"
    
    migrate = Migrate(app, db)

    Bootstrap(app)

    from app import models
    

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from .supplier import supplier as supplier_blueprint
    app.register_blueprint(supplier_blueprint, url_prefix='/supplier')

    from .loader import loader as loader_blueprint
    app.register_blueprint(loader_blueprint, url_prefix='/loader')

    from .recipient import recipient as recipient_blueprint
    app.register_blueprint(recipient_blueprint, url_prefix='/recipient')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    return app
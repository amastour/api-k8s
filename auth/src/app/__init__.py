import os, logging.config

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db= SQLAlchemy()

def create_app(config_type='dev'):
    from app.config import config


    app= Flask(__name__)
    logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), 'logging.conf'))
    app.config.from_object(config[config_type])
    db.init_app(app)
    logging.config.fileConfig(logging_conf_path)

    
    from .v1 import auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/api/v1')

    return app
from flask import Flask
from flask_sqlalchemy import SQLALchemy


db= SQLALchemy()

def create_app(config_type='dev')
    from config import config


    app= Flask(__name__)
    app.config.from_object(config[config_type])
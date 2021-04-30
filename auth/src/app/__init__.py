from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


db= SQLAlchemy()

def create_app(config_type='dev'):
    from config import config


    app= Flask(__name__)
    app.config.from_object(config[config_type])

    db.init_app(app)

    
    @app.route("/ping")
    def ping():
        return jsonify("pong")

    return app
from flask import Blueprint
from flask_restx import Api


auth_blueprint = Blueprint('auth_blueprint',__name__)
auth_api = Api(auth_blueprint,
                title="Auth API",
                version="1.0",
                description="Authentication engine")
import os
import tempfile

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    #SECRET_KEY = 'testing'
    # SQLALCHEMY_DATABASE_URI = 'sqlite://'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, tempfile.mktemp(dir='.', suffix='.db'))
    # tempfile.mktemp(dir=basedir, suffix='.db')TESTING = False
    SECRET_KEY = 'top-secret'
    JWT_SECRET_KEY = SECRET_KEY
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    db_user = 'hero'
    db_pass = 'amaterasu'
    db_name = 'heroku'
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{db_user}:{db_pass}@localhost:3306/{db_name}"


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db_test.db')


class ProductionConfig(Config):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    JWT_SECRET_KEY = SECRET_KEY
    db_user =  os.environ.get('DB_USER','hero')
    db_pass =  os.environ.get('DB_PASS','amaterasu')
    db_name =  os.environ.get('DB_NAME','heroku')
    db_host =  os.environ.get('DB_HOST','localhost')
    db_port =  os.environ.get('DB_PORT',3306)
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"


config = {
    'dev': DevelopmentConfig,
    'test': TestingConfig,
    'prod': ProductionConfig
}

key = Config.SECRET_KEY
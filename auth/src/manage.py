import os

from flask_script import Manager

from app import create_app, db

env = os.getenv("CONFIG_TYPE") or "dev"
app = create_app(env)
manager = Manager(app)




@manager.command
def run():
    """Like a 'runserver' command but shorter, lol."""
    app.run(host="0.0.0.0")


if __name__ == '__main__':
    manager.run()

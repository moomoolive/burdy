from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from burdy.config import Config

cors = CORS()
database = SQLAlchemy()
bcrypt = Bcrypt()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    cors.init_app(app, resource={r'/*': {'origins': '*'}})
    database.init_app(app)
    bcrypt.init_app(app)
    
    from burdy.users.routes import users
    from burdy.main.routes import main

    app.register_blueprint(users)
    app.register_blueprint(main)

    return app
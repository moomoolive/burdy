from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '12007f9421b9dfb9a78f8e969bca67b3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
CORS(app, resource={r'/*': {'origins': '*'}})
database = SQLAlchemy(app)

class Y(database.Model):
    __bind_key__ = 'cool'
    coolio = database.Column(database.Integer, primary_key=True)

from burdy_app import routes

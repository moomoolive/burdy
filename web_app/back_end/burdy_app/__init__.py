from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

app.config['SECRET_KEY'] = '12007f9421b9dfb9a78f8e969bca67b3'
CORS(app, resource={r'/*': {'origins': '*'}})

from burdy_app import routes

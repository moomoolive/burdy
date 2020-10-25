import os

class Config:
    SECRET_KEY = '12007f9421b9dfb9a78f8e969bca67b3'
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL" ,'sqlite:///site.db')
    JWT_SECRET = "%SECretKeyss$$$%"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
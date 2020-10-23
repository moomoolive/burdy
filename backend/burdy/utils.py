from flask import request, jsonify, request
import jwt
from backend.burdy.models import User
import json
from functools import wraps
import datetime
from backend.burdy.config import Config

JWT_SECRET = Config.JWT_SECRET

def check_user(**kwargs):
    user = User.query.filter_by(**kwargs).first()
    return user

def token_required(function):
    @wraps(function)
    def _verify(*args, **kwargs):
        authorization_headers = request.headers.get('Authorization').split()

        if len(authorization_headers) != 2:
            return jsonify('Invalid header'), 401
        
        try:
            token = authorization_headers[1]
            encoded_token = token.encode('ASCII')
            data = jwt.decode(encoded_token, JWT_SECRET, algorithms=['HS256'])
            user = check_user(username=data['user'])
            if not user:
                raise RuntimeError('User not found')
            return function(*args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify('Your token has expired'), 401
        except (jwt.InvalidTokenError, Exception) as e:
            print(e)
            return jsonify('Invalid token'), 403
    return _verify

def create_jwt(user_info, expiration_day=3):
    jwt_token = jwt.encode({
            'user': user_info.username,
            'email': user_info.email,
            'iat': datetime.datetime.utcnow(),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=expiration_day)
            },
            JWT_SECRET
            )
    decoded_token = jwt_token.decode('ASCII')
    return decoded_token
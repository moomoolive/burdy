from flask import request, jsonify, request
import jwt
from burdy_app.models import User
import json
from functools import wraps

with open('security_configurations.json') as f:
    JWT_SECRET = json.load(f)['jwt secret']

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
            user = User.query.filter_by(username=data['user']).first()
            if not user:
                raise RuntimeError('User not found')
            return function(*args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify('Your token has expired'), 401
        except (jwt.InvalidTokenError, Exception) as e:
            print(e)
            return jsonify('Invalid token'), 403
    return _verify
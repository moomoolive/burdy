from flask import request, jsonify
import jwt
from burdy_app.models import User
from functools import wraps
import json

with open('security_configurations.json') as f:
    JWT_SECRET = json.load(f)['jwt secret']

def token_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        authorization_headers = request.headers.get('Authorization', '').split()

        invalid_msg = {
            'message': 'Invalid token. Registeration and / or authentication required',
            'authenticated': False
        }
        expired_msg = {
            'message': 'Expired token. Reauthentication required.',
            'authenticated': False
        }

        if len(authorization_headers) != 2:
            return jsonify(invalid_msg), 401
        
        try:
            token = authorization_headers[1]
            data = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
            user = User.query.filter_by(username=data['sub']).first()
            if not user:
                raise RuntimeError('User Not Found')
            return f(user, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify(expired_msg), 401
        except (jwt.InvalidTokenError, Exception) as e:
            print(e)
            return jsonify(invalid_msg), 401
    
    return _verify
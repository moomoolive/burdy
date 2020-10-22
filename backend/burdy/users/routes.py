from flask import Blueprint, request, jsonify
from burdy.utils import check_user, token_required, create_jwt
from burdy.models import User
from burdy import database, bcrypt

users = Blueprint('users', __name__)

@users.route('/sign_up', methods=['POST'])
def sign_up():
    try:
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
    except:
        return jsonify('Missing Required Data'), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    user = User(username=username, email=email, password=hashed_password)
    database.session.add(user)
    database.session.commit()
    return jsonify(f'Successfully signed up {username} to Burdy!')

@users.route('/check_unique', methods=['POST'])
def check_uniqueness():
    try:
        data = request.get_json()
        check_for = data.get('type')
        value = data.get('data')
        arguments = {check_for: value}
        uniqueness_check = User.query.filter_by(**arguments).first()
    except:
        return jsonify('Missing Required Data'), 400

    if uniqueness_check is not None:
        response = 'not unique'
    else:
        response = 'unique'
    return jsonify(response)

@users.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
    except:
        return jsonify('Missing Required Data'), 400

    user = check_user(username=username)
    if user and bcrypt.check_password_hash(user.password, password):
        jwt_token = create_jwt(user)
        return jsonify(jwt_token)  
    else:
        return jsonify('Invalid username or password'), 401

@users.route('/update_info', methods=['POST'])
@token_required
def update_info():
    try:
        data = request.get_json()
        original_username = data.get('originalUsername')
        new_username = data.get('username')
        new_email = data.get('email')
        print(original_username)
    except:
        return jsonify('Missing Required Data'), 400

    user = check_user(username=original_username)
    if user:
        user.username = new_username
        user.email = new_email
        database.session.commit()
        
        jwt_token = create_jwt(user)
        return jsonify(jwt_token)
    else:
        return jsonify('Profile was not updated!'), 400
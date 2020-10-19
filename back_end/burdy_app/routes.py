from burdy_app import app, database, bcrypt
from flask import flash, jsonify, request, json, render_template
import requests
import tensorflow as tf
from burdy_app.models import User
from burdy_app.utils import token_required, check_user, create_jwt
import random

model = tf.keras.models.load_model('my_model')

@app.route('/', methods=['GET'])
def home():
    return render_template('home_page.html')

@app.route('/review_mine', methods=['POST'])
@token_required
def review_mine():
    try:
        url_data = request.get_json()
        url = url_data.get('url')
    except:
        return jsonify('Missing Required Data'), 400

    try:
        path = "http://localhost:9080/crawl.json?spider_name=burdy_scraper&url="
        scrapy_request = requests.get(path + url)
    except requests.Timeout:
        return jsonify('Scrapy service is probably not active, check back later'), 408
    except Exception:
        return jsonify('Scrapy service error'), 500
    data = scrapy_request.json()['items']

    return_dict = {
        0: [],
        1: [],
        2: [],
        3: []
    }
    for opinion_unit in data:
        if opinion_unit['Opinion Unit'] == '':
            data.remove(opinion_unit)
            continue
        tensor = tf.constant([opinion_unit['Opinion Unit']], dtype=tf.string)
        prediction = round(model.predict(tensor)[0][0] + (random.random() * 3))
        if prediction <= 0:
            prediction *= -1
        return_dict[prediction].append(opinion_unit['Opinion Unit'])
    
    return jsonify(return_dict)

@app.route('/sign_up', methods=['POST'])
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

@app.route('/check_unique', methods=['POST'])
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

@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
    except:
        return jsonify('Missing Required Data'), 400

    user = check_user(user_name=username)
    if user and bcrypt.check_password_hash(user.password, password):
        jwt_token = create_jwt(user)
        return jsonify(jwt_token)  
    else:
        return jsonify('Invalid username or password'), 401

@app.route('/update_info', methods=['POST'])
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

    user = check_user(user_name=original_username)
    if user:
        user.username = new_username
        user.email = new_email
        database.session.commit()
        
        jwt_token = create_jwt(user)
        return jsonify(jwt_token)
    else:
        return jsonify('Profile was not updated!'), 400


    
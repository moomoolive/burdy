from burdy_app import app, database, bcrypt
from flask import flash, jsonify, request, json, render_template
import requests
import tensorflow as tf
from burdy_app.models import User
import jwt
import json
import datetime

model = tf.keras.models.load_model('my_model')
with open('security_configurations.json') as f:
    JWT_SECRET = json.load(f)['jwt secret']

@app.route('/', methods=['GET'])
def home():
    return render_template('home_page.html')

@app.route('/review_mine', methods=['POST'])
def review_mine():
    data = {'status': 'success'}

    if request.method == 'POST':
        path = "http://localhost:9080/crawl.json?spider_name=burdy_scraper&url="

        url_data = request.get_json()
        url = url_data.get('url')
        scrapy_request = requests.get(path + url)
        data = scrapy_request.json()['items']
        for opinion_unit in data:
            if opinion_unit['Opinion Unit'] == '':
                data.remove(opinion_unit)
                continue
            tensor = tf.constant([opinion_unit['Opinion Unit']], dtype=tf.string)
            prediction = model.predict(tensor)[0][0]
            if prediction < 0:
                prediction *= -1
            opinion_unit['Classification'] = str(prediction)
        
        return jsonify(data)

    return jsonify(data)

@app.route('/sign_up', methods=['POST'])
def sign_up():
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        user = User(username=username, email=email, password=hashed_password)
        database.session.add(user)
        database.session.commit()

        return jsonify(f'Successfully signed up {username} to Burdy!')

    return 'Sign up'

@app.route('/check_unique', methods=['POST'])
def check_uniqueness():
    if request.method == 'POST':
        data = request.get_json()
        check_for = data.get('type')
        value = data.get('data')
        arguments = {check_for: value}
        uniqueness_check = User.query.filter_by(**arguments).first()

        response = None
        if uniqueness_check is not None:
            response = 'not unique'
        else:
            response = 'unique'
        return jsonify(response)
        
    return 'Check Uniqueness'

@app.route('/authenticate', methods=['POST'])
def authenticate():
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            jwt_token = jwt.encode({
                'sub': username,
                'iat': datetime.datetime.utcnow(),
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
                }, 
                JWT_SECRET
                )
            return jsonify(str(jwt_token))  
        else:
            return jsonify('Invalid username or password')

    return 'authenticate'
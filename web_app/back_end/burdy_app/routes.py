from burdy_app import app, database, bcrypt
from flask import flash, jsonify, request, json, render_template
import requests
import tensorflow as tf
from burdy_app.models import User

model = tf.keras.models.load_model('my_model')

@app.route('/', methods=['GET'])
def home():
    return render_template('home_page.html')

@app.route('/review_mine', methods=['POST'])
def review_mine():
    data = {'status': 'success'}

    if request.method == 'POST':
        data = request.get_json()
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

@app.route('/sign_up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        print(username, email, password, hashed_password)

        user = User(username=username, email=email, password=hashed_password)
        database.session.add(user)
        database.session.commit()

        return jsonify(username, email, password)

    return 'Sign up'

@app.route('/check_unique', methods=['GET', 'POST'])
def check_uniqueness():
    if request.method == 'POST':
        data = request.get_json()
        check_for = data.get('type')
        value = data.get('data')
        arguments = {check_for: value}
        uniqueness_check = User.query.filter_by(**arguments).first()

        response = None
        if uniqueness_check is not None:
            response = jsonify('false')
        else:
            response = jsonify('true')
        return response
        
    return 'hello world'
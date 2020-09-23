from burdy_app import app
from flask import flash, jsonify, request, json
import requests
import tensorflow as tf

model = tf.keras.models.load_model('my_model')

@app.route('/', methods=['GET'])
def home():
    return '<h1>Welcome to the homepage of Burdy API</h1>'

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/review_mine', methods=['GET', 'POST'])
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


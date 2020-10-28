from flask import Flask, request, jsonify
from flask.cli import FlaskGroup
from flask_cors import CORS
import tensorflow as tf
import random

app = Flask(__name__)
cli = FlaskGroup(app)
cors = CORS(app, resources={r"/*": {'origins': '*'}})

tensorflow_model = tf.keras.models.load_model('my_model')

@app.route('/', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        reviews = data.get('reviews')
    except Exception as e:
        print(e)
        return jsonify('Missing Required Data'), 400
    
    return_dict = {
        0: [],
        1: [],
        2: [],
        3: []
    }
    
    for opinion_unit in reviews:
        if opinion_unit['Opinion Unit'] == '':
            reviews.remove(opinion_unit)
            continue
        tensor = tf.constant([opinion_unit['Opinion Unit']], dtype=tf.string)
        prediction = round(tensorflow_model.predict(tensor)[0][0] + (random.random() * 3))
        if prediction <= 0:
            prediction *= -1
        return_dict[prediction].append(opinion_unit['Opinion Unit'])

    return jsonify(return_dict)

if __name__ == '__main__':
    cli()
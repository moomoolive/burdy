from flask import Blueprint, render_template, jsonify, request
import requests
import tensorflow as tf
import random
from burdy.utils import token_required
import tensorflow as tf
from burdy.config import Config
#from burdy import tensorflow_model

main = Blueprint('main', __name__)

service = Config.SCRAPER_SERVICE

@main.route('/', methods=['GET'])
def home():
    return render_template('home_page.html')

@main.route('/review_mine', methods=['POST'])
@token_required
def review_mine():
    try:
        url_data = request.get_json()
        url = url_data.get('url')
    except:
        return jsonify('Missing Required Data'), 400

    try:
        path = f"http://{service}:9080/crawl.json?spider_name=burdy_production&url="
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
    # Fix tensorflow import problem
    """
    for opinion_unit in data:
        if opinion_unit['Opinion Unit'] == '':
            data.remove(opinion_unit)
            continue
        tensor = tf.constant([opinion_unit['Opinion Unit']], dtype=tf.string)
        prediction = round(tensorflow_model.predict(tensor)[0][0] + (random.random() * 3))
        if prediction <= 0:
            prediction *= -1
        return_dict[prediction].append(opinion_unit['Opinion Unit'])"""
    
    return jsonify(return_dict)
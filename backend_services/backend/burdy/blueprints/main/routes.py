from flask import Blueprint, render_template, jsonify, request
import requests
from burdy.utils import token_required
from burdy.config import Config

main = Blueprint('main', __name__)

scraper = Config.SCRAPER_SERVICE
tensorflow_API = Config.TENSORFLOW

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
        path = f"http://{scraper}:9080/crawl.json?spider_name=burdy_production&url="
        scrapy_request = requests.get(path + url)
    except requests.Timeout:
        return jsonify('Scrapy service is probably not active, check back later'), 408
    except Exception:
        return jsonify('Scrapy service error'), 500
    
    data = scrapy_request.json()['items']
    amazon_reviews = {'reviews': data}
    print(amazon_reviews)

    try:
        path = f"http://{tensorflow_API}:5001/"
        tensorflow_request = requests.post(path, json=amazon_reviews)
    except Exception as e:
        print(e)

    return_dict = tensorflow_request.json()
    
    return jsonify(return_dict)
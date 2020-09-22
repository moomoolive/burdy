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
        post_data = request.get_json()
        url = post_data.get('url')
        path = f"http://localhost:9080/crawl.json?spider_name=burdy_scraper&url={url}"
        response = requests.get(path)
        
        # returns dict
        data = response.json()
        for item in data['items']:
            #if item['Opinion Unit'] == '':
               # data['items'].remove(item)
                #continue
            #item['Classification'] = model.predict(item['Opinion Unit'])
            print(item['Opinion Unit'] + " : " )
        
        return jsonify(data)

    return jsonify(data)


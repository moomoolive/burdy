from burdy_app import app
from flask import flash, jsonify, request


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/review_mine', methods=['POST'])
def review_mine():
    response_object = {'status': 'success'}

    if request.method == 'POST':
        post_data = request.get_json()
        response_object['message'] = 'Successfully updated resource'
    
    return response_object


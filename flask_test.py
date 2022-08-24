#!/usr/bin/env/ python

from flask import Flask, request
import json
from flask_cors import CORS

app = Flask(__name__, static_folder='.', static_url_path='')
cors = CORS(app, supports_credentials=True, allow_headers="Content-Type")


@app.route('/service', methods=['POST'])
def service_callback():
    # print(f'data\n{request}')
    data = json.loads(request.data.decode('utf-8'))
    print(f'data\n{data}')
    # service = data['service']
    # ros_type = data['type']
    # payload = data['payload']
    # response is not yet supported
    return 'Done'


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,PUT,POST,DELETE,OPTIONS')
    return response


app.run(debug=True, port=5555, host='0.0.0.0', use_reloader=False)

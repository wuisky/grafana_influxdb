#!/usr/bin/env/ python

import json
from flask import Flask, request
from flask_cors import CORS  #, cross_origin

app = Flask(__name__, static_folder='.', static_url_path='')
cors = CORS(app, supports_credentials=True, allow_headers='Content-Type')


@app.route('/service', methods=['OPTIONS'])
def option_callback():
    # print('option')
    print(f'header\n{request.headers}')
    print(f'arg\n{request.args}')
    return 'Done'


@app.route('/service', methods=['POST'])
def service_callback():
    print(f'Aparam is {request.headers["Aparam"]}')
    # print(f'arg\n{request.args}')
    # print(f'form\n{request.form}')
    # print(f'values\n{request.values}')
    print(f'header\n{request.headers}')
    data = json.loads(request.data.decode('utf-8'))
    print(f'data\n{data}')
    # service = data['service']
    # ros_type = data['type']
    # payload = data['payload']
    # call_service(service, ros_type, payload)
    # response is not yet supported
    return 'Done'


@app.after_request
def after_request(response):
    # print('after')
    # response.headers['Access-Control-Allow-Origin'] = request.environ.get(
    #     'HTTP_ORIGIN')
    # response.headers.add('Access-Control-Allow-Origin', '*')
    # response.headers.add('Access-Control-Allow-Headers', '*')
    # response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization,Aparam')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,PUT,POST,DELETE,OPTIONS')
    # print(f'{response.headers}')
    return response


app.run(debug=True, port=5555, host='0.0.0.0', use_reloader=False)

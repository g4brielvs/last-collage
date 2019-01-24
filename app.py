#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""app.py: Python Serverless Microframework"""

import json

from chalice import Chalice, Response
from chalicelib.helpers import upload_to_s3

app = Chalice(app_name='app')

@app.route('/')
def index():

    body = {'code': 200, 'message': 'Everything is up and running!'}

    return Response(body=json.dumps(body),
                    status_code=200,
                    headers={'Content-Type': 'application/json'})


@app.route('/upload', methods=['PUT'], content_types=['application/octet-stream'])
def upload():

    # get raw body of PUT request
    data = app.current_request.raw_body

    # upload to S3
    url = upload_to_s3(data) 

    body = {'url' : url}
    
    return Response(body=json.dumps(body),
                    status_code=201,
                    headers={'Content-Type': 'application/json'})


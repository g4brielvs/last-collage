#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""app.py: Python Serverless Microframework"""

import os
import io
import json

import pytest 

from chalice import Chalice, Response
from chalicelib.main import upload_obj_to_s3, get_images, create_collage

app = Chalice(app_name='g4brielvs-last-collage')

@app.route('/')
def index():
    
    body = {'code': 200, 'message': 'Everything is up and running!'}

    status = None#pytest.main(['-x', 'chalicelib/tests.py'])
    if status:
            body = {'code': 500, 
                    'message': 'Something went wrong. The API is not available.',
                    'status': status}
            
    return Response(body=json.dumps(body),
                    status_code=200,
                    headers={'Content-Type': 'application/json'})

@app.route('/collage/{user}')
def collage(user):

    images = get_images(user)
    im = create_collage(images)

    # buffering
    buffer = io.BytesIO()
    im.save(buffer, "PNG")
    buffer.seek(0)
    
    # upload to S3
    url = upload_obj_to_s3(buffer) 

    response = {'url' : url}
    return Response(body=json.dumps(response),
                    status_code=201,
                    headers={'Content-Type': 'application/json'})

@app.route('/upload', methods=['POST'], content_types=['application/octet-stream'])
def upload():

    # get raw body of PUT request
    body = app.current_request.raw_body
    buffer = io.BytesIO(body)

    # upload to S3
    url = upload_obj_to_s3(buffer) 

    response = {'url' : url}
    return Response(body=json.dumps(response),
                    status_code=201,
                    headers={'Content-Type': 'application/json'})
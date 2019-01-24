#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""app.py: Python Serverless Microframework"""

import json

from chalice import Chalice, Response
from chalicelib import helpers

app = Chalice(app_name='app')

@app.route('/')
def index():

    body = {'code': 200, 'message': 'Everything is up and running!'}

    return Response(body=json.dumps(body),
                    status_code=200,
                    headers={'Content-Type': 'application/json'})


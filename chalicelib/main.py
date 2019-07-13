#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""main.py: Main"""

import os
import hashlib
import requests
import uuid

from io import BytesIO
from PIL import Image, ImageDraw

from boto3 import client 

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_BUCKET = os.environ['AWS_BUCKET']
LASTFM_SECRET = os.environ['LASTFM_SECRET']

def upload_obj_to_s3(obj):

    S3 = client('s3', 
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name='us-east-1')
    try:
        key = uuid.uuid4().hex
        S3.upload_fileobj(
            obj,
            AWS_BUCKET,
            key,           
            ExtraArgs={
                "ACL": "public-read",
                "ContentType": 'image/png'
            }
        )

    except Exception as e:
        return e

    return f'https://s3.amazonaws.com/{AWS_BUCKET}/{key}'

def get_images(user):

    url = "http://ws.audioscrobbler.com/2.0/"
    body = {
        'method': 'user.gettopalbums',
        'user': user,
        'api_key': LASTFM_SECRET,
        'limit': 16,
        'period': 'overall',
        'format': 'json'
    }
    r = requests.get(url, body)

    items = r.json()['topalbums']['album']
    images = []
    for item in items:
        image_url = item['image'][3]['#text']
        if image_url:
            r = requests.get(image_url)
            image = {
                'name': item['name'],
                'data': r.content
            }
            images.append(image)
    return images
            
def create_collage(cells, rows=4, cols=4):
    
    w, h = Image.open(BytesIO(cells[0]['data'])).size
    collage_width = cols * w
    collage_height = rows * h
    collage = Image.new('RGB', (collage_width, collage_height))
    cursor = (0,0)
    for cell in cells:
        # place image
        collage.paste(Image.open(BytesIO(cell['data'])), cursor)
        # move cursor
        y = cursor[1]
        x = cursor[0] + w
        if cursor[0] >= (collage_width - w):
            y = cursor[1] + h
            x = 0
        cursor = (x, y)

    return collage
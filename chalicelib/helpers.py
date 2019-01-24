#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""helpers.py: Helpers"""

import hashlib
import os
import uuid

from io import BytesIO

from boto3 import client 

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
BUCKET = os.environ['BUCKET']

def upload_to_s3(input_data):
    
    data = BytesIO()
    data.write(input_data)
    data.seek(0)

    S3 = client('s3', 
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name='us-east-1')

    key = uuid.uuid4().hex

    try:
        S3.upload_fileobj(
            data,
            BUCKET,
            key,           
            ExtraArgs={
                "ACL": "public-read",
                "ContentType": 'image/png'
            }
        )

    except Exception as e:
        return e

    return f'https://s3.amazonaws.com/{BUCKET}/{key}'
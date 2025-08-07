from flask import (
    Flask,
    flash,
    request,
    redirect,
    url_for,
    jsonify,
    send_from_directory,
    after_this_request,
)
from flask_cors import CORS

import threading
import json

import boto3
import botocore.exceptions

app = Flask(__name__)
#TODO secure this?
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
CORS(app)

s3 = boto3.client('s3')

@app.route("/pfp-upload-url")
def PFPUploadUrl():
    #todo precheck for auth

    # todo get s3 config
    bucket_name = 'testbucket-jluow'
    key = 'image1'  # Path inside the bucket
    max_size_bytes = 5 * 1024 * 1024  # 5 MB

    expiration = 300  # URL valid for 5 min

    try:
        post = s3.generate_presigned_post(
            Bucket=bucket_name,
            Key=key,
            Fields={"Content-Type": "image/jpeg"},
            Conditions=[
                ["starts-with", "$Content-Type", "image/"],
                ["content-length-range", 1, max_size_bytes]
            ],
            ExpiresIn=expiration
        )

        print("Presigned URL:", post)

        # curl -X POST \
        # -F "key=uploads/image.jpg" \
        # -F "Content-Type=image/jpeg" \
        # -F "AWSAccessKeyId=..." \
        # -F "policy=..." \
        # -F "signature=..." \
        # -F "file=@yourimage.jpg" \
        # https://your-bucket-name.s3.amazonaws.com/

        return post

    except botocore.exceptions.NoCredentialsError:
        print("AWS credentials not found.")

@app.route("/find-lobby")
def list_lobbies():
    return "not yet done"
import os
import base64
import json
import boto3


def file_view_handler(event, context):
    s3 = boto3.client('s3')
    S3_FILE_CACHE_BUCKET_NAME = os.environ['S3_FILE_CACHE_BUCKET_NAME']
    params = event['pathParameters']
    folder_id = params['FOLDER_ID']
    file_id = params['FILE_ID']
    s3_key = '{}/{}'.format(folder_id, file_id)
    s3_object = s3.get_object(
        Bucket=S3_FILE_CACHE_BUCKET_NAME, Key=s3_key)

    if file_id == 'screen.png':
        response = {
            "statusCode": 200,
            "headers": {
                "Content-Type": "image/png"
                },
            "body": base64.b64encode(s3_object['Body'].read()).decode('utf-8'),
            "isBase64Encoded": True
        }
    else:
        response = {
            "statusCode": 200,
            "headers": {
                "Content-Type": "image/jpeg"
                },
            "body": base64.b64encode(s3_object['Body'].read()).decode('utf-8'),
            "isBase64Encoded": True
        }
    return response
# "body": base64.b64encode(s3_object['Body'].read()),

import json
import boto3

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Good Day from CloudBot!')
    }

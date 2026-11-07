import json
import os
import boto3

secret_name = os.environ.get('SECRET_NAME', '')
client_secretsmanager = boto3.client('secretsmanager', region_name='us-west-2')


def handler(event, context):
    print(json.dumps(event))
    response = client_secretsmanager.get_secret_value(
        SecretId=secret_name
    )
    print(response)
    owner = response['SecretString']['owner']
    env = response['SecretString']['env']
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({
            "message_lambda": "Hello World from Ivan!",
            "message": "Hardcoded message",
            "owner": owner,
            "env": env,
        }),
    }

import json
import sys


def handler(event, context):
    debug=True

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({
            "message_lambda": "Hello World!",
            "message": "Hardcoded message",
            "owner": "Hardcoded owner",
            "env": "hardcoded",
        }),
    }

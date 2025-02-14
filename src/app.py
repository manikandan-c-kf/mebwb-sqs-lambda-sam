import json

def lambda_handler(event, context):
    print("Lambda function event -- ", event)
    return {
        'statusCode': 200,
        'body': json.dumps('SQS messages processed successfully!')
    }
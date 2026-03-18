import json
import boto3
import base64
import uuid
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('telemax-data')

def lambda_handler(event, context):
    print(f"Received {len(event['Records'])} records from Kinesis")
    
    for record in event['Records']:
        # Decode the Kinesis data (arrives as base64)
        payload = base64.b64decode(record['kinesis']['data']).decode('utf-8')
        data = json.loads(payload, parse_float=Decimal)
        
        # Add unique ID for DynamoDB partition key
        data['record_id'] = str(uuid.uuid4())
        
        # Write to DynamoDB
        table.put_item(Item=data)
        print(f"Saved record: {data['record_id']} | device: {data['device_id']}")
    
    return {
        'statusCode': 200,
        'body': json.dumps(f"Successfully processed {len(event['Records'])} records")
    }
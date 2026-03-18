import boto3
import json
import time
import random
from decimal import Decimal

# Configure your region
kinesis = boto3.client('kinesis', region_name='us-east-1')

STREAM_NAME = 'telemax-stream'

def generate_record():
    return {
        "device_id": f"tower-{random.randint(1, 50)}",
        "signal_strength": random.randint(-100, 0),
        "bandwidth_mbps": round(random.uniform(1.0, 100.0), 2),
        "location": random.choice(["Lagos", "Nairobi", "Mumbai", "Jakarta"]),
        "timestamp": str(time.time())
    }

def send_to_kinesis(record):
    response = kinesis.put_record(
        StreamName=STREAM_NAME,
        Data=json.dumps(record),
        PartitionKey=record['device_id']
    )
    return response

if __name__ == '__main__':
    print(f"Starting data producer for stream: {STREAM_NAME}")
    for i in range(10):
        record = generate_record()
        response = send_to_kinesis(record)
        print(f"Sent record {i+1}/10: {record}")
        time.sleep(0.5)
    print("Done! All records sent to Kinesis.")
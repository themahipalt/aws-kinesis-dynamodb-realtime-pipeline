# AWS Kinesis → DynamoDB Real-Time Pipeline

## Project Overview
Real-time data pipeline built for TELEMAX using:
- **Amazon Kinesis Data Streams** — real-time data ingestion
- **AWS Lambda** — serverless event processing
- **Amazon DynamoDB** — NoSQL data storage

## Architecture
```
[Producer] → [Kinesis Stream] → [Lambda] → [DynamoDB]
```

## Folder Structure
```
aws-kinesis-dynamodb-realtime-pipeline/
├── producer/producer.py          # Sends data to Kinesis
├── lambda/lambda_function.py     # Processes and saves to DynamoDB
├── infrastructure/               # CloudFormation YAML templates
├── screenshots/                  # AWS Console screenshots
├── architecture/                 # Architecture diagram
└── docs/project-explanation.md   # Detailed documentation
```

## Setup Steps
1. Create IAM Role with Kinesis, DynamoDB, CloudWatch permissions
2. Create Kinesis Data Stream — `telemax-stream`
3. Create DynamoDB Table — `telemax-data`
4. Deploy Lambda Function — `kinesis-to-dynamodb`
5. Add Kinesis trigger to Lambda
6. Run producer script to send test data
7. Verify records in DynamoDB

## Requirements
- Python 3.12
- boto3
- AWS Account with appropriate permissions

## Author
TELEMAX Infrastructure Team
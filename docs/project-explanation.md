
### Folder Structure
~~~
aws-kinesis-dynamodb-realtime-pipeline
│
├── README.md
├── architecture
│     └── architecture-diagram.png
│
├── producer
│     └── producer.py
│
├── lambda
│     └── lambda_function.py
│
├── infrastructure
│     ├── kinesis-stream.yaml
│     ├── lambda.yaml
│     └── dynamodb.yaml
│
├── screenshots
│     ├── kinesis-stream.png
│     ├── dynamodb-table.png
│     ├── lambda-trigger.png
│
└── docs
      └── project-explanation.md
~~~


# TELEMAX Real-Time Data Pipeline — Project Explanation

## Overview
This project implements a real-time data pipeline on AWS for TELEMAX,
a telecommunications company building networks in underserved markets.

## Architecture
Data flows through 3 main AWS services:

Producer → Kinesis Data Stream → Lambda Function → DynamoDB

## Components

### 1. Kinesis Data Stream (telemax-stream)
- Ingests real-time data from network towers
- 1 shard handles up to 1,000 records/second
- Retains data for 24 hours

### 2. Lambda Function (kinesis-to-dynamodb)
- Automatically triggered when new data arrives in Kinesis
- Decodes base64 encoded records
- Converts float values to Decimal for DynamoDB compatibility
- Writes processed records to DynamoDB

### 3. DynamoDB Table (telemax-data)
- NoSQL database storing all tower records
- Partition key: record_id (unique UUID per record)
- Pay-per-request billing — scales automatically

## Data Schema
Each record contains:
| Field            | Type    | Description                        |
|------------------|---------|------------------------------------|
| record_id        | String  | Unique identifier (UUID)           |
| device_id        | String  | Tower identifier e.g. tower-23     |
| signal_strength  | Number  | Signal in dBm (-100 to 0)          |
| bandwidth_mbps   | Decimal | Bandwidth in Mbps                  |
| location         | String  | City name                          |
| timestamp        | String  | Unix timestamp of the record       |

## How to Run

### Step 1 — Send data to Kinesis
```bash
cd producer
python3 producer.py
```

### Step 2 — Verify in DynamoDB
- Go to AWS Console → DynamoDB → telemax-data
- Click Explore table items
- Click Run to see all records

## IAM Permissions Required
- AmazonKinesisFullAccess
- AmazonDynamoDBFullAccess
- CloudWatchLogsFullAccess

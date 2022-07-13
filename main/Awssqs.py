from http import client
import json
import boto3

from dotenv import load_dotenv
import os

load_dotenv()

aws_secret_access_key = os.getenv("ACCESSKEY")
aws_access_key_id=os.getenv("ACCESSID")
region_name=os.getenv("REGION")
QueueUrl=os.getenv("QUEUEURL")

client = boto3.client('sqs',aws_secret_access_key = aws_secret_access_key ,aws_access_key_id = aws_access_key_id,region_name=region_name)
QueueUrl=QueueUrl
queue='counterQueue.fifo'
print(client)


def poll():

    response = client.receive_message(
        QueueUrl=QueueUrl,
        MaxNumberOfMessages=1,
    )

    receipt=response["Messages"][0]['ReceiptHandle']
    # print(receipt)

    client.delete_message(QueueUrl=QueueUrl, ReceiptHandle=receipt)  



    # print(json.dumps(response , indent= 4))
    return response






import boto3
import time
client = boto3.resource('dynamodb')

table = client.Table('urlshortenerTable')


def put_item(short , long , count):
    item = table.put_item(Item={'shortUrl':short,'counter':count , 'longUrl':long,'url_ttl':int(time.time()+300)})
    print(item)
    return item

def get_item(short):
    x = table.get_item(Key={'shortUrl':short})
    return x


# put_item('gndnsn','dshtgdlsz','1')
# get_item('gndnsn')








# def create_table():
    
#     table = client.create_table(
#         TableName='urlshortenerTable',
#         KeySchema=[ 
#             {
#                 'AttributeName': 'shortUrl',
#                 'KeyType': 'HASH'
#             }
#         ],
#         AttributeDefinitions=[
#             {
#                 'AttributeName': 'shortUrl',
#                 'AttributeType': 'S'
#             }
#          ],
#          ProvisionedThroughput={
#              'ReadCapacityUnits': 1,
#              'WriteCapacityUnits': 1
#          }
#     )
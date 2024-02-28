import boto3
import json


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('mycrcvisittb')
def lambda_handler(event, context):

  # GetItem = dynamodb.get_item(
  #   TableName='mycrcvisittb',
  #   Key={
  #       'visitcount': {
  #         'S': '2'
  #       }
  #   }
  # )
  # response = {
  #     'statusCode': 200,
  #     'body': json.dumps(GetItem)
  # }

  countincrease = table.update_item(
      # TableName='mycrcvisittb',
      Key={
          'visitcount': 'vcount'
      }, 
      UpdateExpression='SET vcount = vcount + :val',  
      ExpressionAttributeValues={
          ':val': 1
      },
      ReturnValues="UPDATED_NEW"
  )
  # response = {
  #     'statusCode': 200,
  #     'body': json.dumps(countincrease)
  # }
  return countincrease

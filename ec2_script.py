import boto3
import requests
import sys

dynamo_res = boto3.resource('dynamodb','us-east-1')
s3_res = boto3.client('s3')

# change the bucket names 
input_bucket_name = 'akhi-input-bucket'
output_bucket_name = 'akhi-output-bucket'

id= int(sys.argv[1])

input_table_name='Dynamo_input-s3-db'
output_table_name='Dynamo_output-s3-db'

table = dynamo_res.Table(input_table_name)
response=table.get_item(Key={"id":id})

inputText=response['Item']['inputText']

file=requests.get(response['Item']['inputS3Path'])

s3_res.put_object(Bucket=output_bucket_name,Key="output_"+str(id)+'.txt',Body=file.content.decode()+" : " + inputText)
s3_path = s3_res.generate_presigned_url(ClientMethod='get_object',Params={'Bucket':output_bucket_name,'Key':"output_"+str(id)+'.txt'})

output_table = dynamo_res.Table(output_table_name)
res = output_table.put_item(
    Item={ 'id':id, 'outputS3Path':s3_path })
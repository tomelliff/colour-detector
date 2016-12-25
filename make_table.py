import boto3

dynamodb = boto3.resource('dynamodb', region_name='eu-west-1', endpoint_url='http://localhost:8000')

table = dynamodb.create_table(
    TableName='ProductColours',
    KeySchema=[
        {
            'AttributeName': 'rgb_values',
            'KeyType': 'HASH'  #Partition key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'rgb_values',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print('Table status:', table.table_status)

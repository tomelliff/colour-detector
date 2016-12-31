Takes an image, finds the dominant colour in the image and then matches that to a product sold on the Wickes website.

### Running it locally

#### Install requirements
```
virtualenv env
. env/bin/activate
pip install -r requirements.txt
```

[Set up DynamoDB Local](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html):
1. Download [_.tar.gz_ format](http://dynamodb-local.s3-website-us-west-2.amazonaws.com/dynamodb_local_latest.tar.gz) or [_.zip_ format](http://dynamodb-local.s3-website-us-west-2.amazonaws.com/dynamodb_local_latest.zip)
2. Extract to location of your choice
3. Navigate to the extracted directory and run:
```
java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb
```
to start DynamoDB locally.

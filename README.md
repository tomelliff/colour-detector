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
3. To start DynamoDB locally, navigate to the extracted directory and run:

    ```
    java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb
    ```

#### Authenticate with Google Cloud (to use the Vision API)
[Install Google Cloud SDK](https://cloud.google.com/sdk/docs/quickstart-linux)

1. Download [64 bit](https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-138.0.0-linux-x86_64.tar.gz) or [32 bit](https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-138.0.0-linux-x86.tar.gz) tarball
2. Extract to location of your choice
3. Navigate to the extracted directory and run:

    ```
    ./google-cloud-sdk/install.sh
    ```
    
4. Initialise the SDK:

    ```
    gcloud init
    ```
    
5. Authenticate:

    ```
    gcloud beta auth application-default login
    ```

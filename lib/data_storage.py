import os

import boto3
from botocore.exceptions import ClientError

class DataStorage(object):
    """
    Store RGB values against product code and retrieve product codes for
    given RGB values.
    """

    def __init__(self, local=False, region=None, table_name='ProductColours'):
        if local:
            self._dynamodb = boto3.resource(
                            'dynamodb',
                            aws_secret_access_key='dummyKey',
                            aws_access_key_id='dummyKey',
                            region_name='us-east-1',
                            endpoint_url='http://localhost:8000')
        else:
            region = os.environ.get('AWS_DEFAULT_REGION', region)
            if region is None:
                raise ValueError('You must specify either local or a region')
            self._dynamodb = boto3.resource(
                                            'dynamodb',
                                            region_name=region,
                                            endpoint_url='https://dynamodb.{}.amazonaws.com'.format(region))
        self._table = self._dynamodb.Table(table_name)

    def _convert_rgb_string_to_tuple(self, rgb_string):
        """
        Takes a string of RGB values and converts it into a tuple.
        Example input: '086103001'
        Example output: (86, 103, 1)
        """

        return tuple([int(rgb_string[0:3]), int(rgb_string[3:6]), int(rgb_string[6:9])])


    def _convert_rgb_tuple_to_string(self, rgb_tuple):
        """
        Takes a tuple of RGB values and formats it into a string.
        Example input: (86, 103, 1)
        Example output: '086103001'
        """

        return ''.join([self._zero_pad_number(v) for v in rgb_tuple])

    def _zero_pad_number(self, number, length=3):
        return str(number).zfill(length)

    def store_product_for_rgb(self, rgb, product_code):
        """Store the product code against the RGB values."""

        rgb_values = self._convert_rgb_tuple_to_string(rgb)

        response = self._table.put_item(
            Item={
                'rgb_values': rgb_values,
                'product_code': product_code
            }
        )

        return response

    def get_product_for_rgb(self, rgb):
        """Get product codes for an inputted RGB tuple."""

        rgb_values = self._convert_rgb_tuple_to_string(rgb)

        try:
            response = self._table.get_item(
                Key={
                    'rgb_values': rgb_values
                }
            )
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            if 'Item' in response:
                return response['Item']['product_code']

    def get_all_rgb_values(self):
        """Get all stored RGB values."""

        rgb_values = []
        response = self._table.scan()
        for item in response['Items']:
            rgb_values.append(self._convert_rgb_string_to_tuple(item['rgb_values']))

        return rgb_values

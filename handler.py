import json
import os
import sys

here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "lib"))

import product_finder

def handler(event, context):
    print('event', event)
    if 'body' in event:
        json_body = json.loads(event['body'])
        base64_image = json_body['base64_image']
    else:
        base64_image = event['base64_image']
    closest_match = product_finder.find_product(table_name='ProductColours', image_content=base64_image)

    response = {
        "statusCode": 200,
        "body": json.dumps({'product_code': closest_match[0], 'delta': closest_match[1]})
    }

    return response

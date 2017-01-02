import os
import sys

here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "lib"))

import product_finder

def handler(event, context):
    print('event', event)
    base64_image = event['base64_image']
    closest_match = product_finder.find_product(table_name='ProductColours', image_content=base64_image)

    response = {
        "statusCode": 200,
        "body": closest_match
    }

    return response

#!/usr/bin/env python

import argparse
import base64

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

"""
Detects dominant colour in an image using Google's Vision API.
Based largely around https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/vision/api/label/label.py

Usage: ./colour_detector.py [image]
"""

def main(photo_file):
    """Find the RGB values of the dominant colour in a single image"""

    credentials = GoogleCredentials.get_application_default()
    service = discovery.build('vision', 'v1', credentials=credentials)

    with open(photo_file, 'rb') as image:
        image_content = base64.b64encode(image.read())
        service_request = service.images().annotate(body={
            'requests': [{
                'image': {
                    'content': image_content.decode('UTF-8')
                },
                'features': [{
                    'type': 'IMAGE_PROPERTIES',
                    'maxResults': 1
                }]
            }]
        })

        response = service_request.execute()
        #print(response)
        rgb_values = response['responses'][0]['imagePropertiesAnnotation']['dominantColors']['colors'][0]['color']
        print('Dominant colour RGB: %s for %s' % (rgb_values, photo_file))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image_file', help='The image you\'d like to get the colour for.')
    args = parser.parse_args()
    main(args.image_file)

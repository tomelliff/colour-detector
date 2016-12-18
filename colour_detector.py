#!/usr/bin/env python

import argparse
import base64

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

class ColourDetector(object):
    """
    Detects dominant colour in an image using Google's Vision API.
    Based largely around https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/vision/api/label/label.py
    """

    def get_rgb_values(self, photo_file):
        """
        Find the RGB values of the dominant colour in a single image
        Returns a tuple of RGB values
        """

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
            rgb_values = response['responses'][0]['imagePropertiesAnnotation']['dominantColors']['colors'][0]['color']
            red = rgb_values['red']
            green = rgb_values['green']
            blue = rgb_values['blue']
            return (red, green, blue)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image_file', help='The image you\'d like to get the colour for.')
    args = parser.parse_args()

    cd = ColourDetector()
    rgb_values = cd.get_rgb_values(args.image_file)
    print(rgb_values)

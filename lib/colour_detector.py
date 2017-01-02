import os
import sys

here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "../vendored"))

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

class ColourDetector(object):
    """
    Detects dominant colour in an image using Google's Vision API.
    Based largely around https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/vision/api/label/label.py
    """

    def get_rgb_values(self, image_content):
        """
        Find the RGB values of the dominant colour in a single image.
        image_content is a base64 encoded image file.
        Returns a tuple of RGB values.
        """

        here = os.path.dirname(os.path.realpath(__file__))

        credentials_path = os.path.join(here, "../google-application-credentials.json")
        if os.path.isfile(credentials_path) and os.path.getsize(credentials_path) > 0:
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

        credentials = GoogleCredentials.get_application_default()
        service = discovery.build('vision', 'v1', credentials=credentials)

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
        # If an RGB value is not present then the Google Vision API doesn't return a key in the color object
        # The rgb key also returns undefined strings
        red = rgb_values.get('red', 0)
        green = rgb_values.get('green', 0)
        blue = rgb_values.get('blue', 0)
        return (red, green, blue)

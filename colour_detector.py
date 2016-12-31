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
        # Black returns an empty color dictionary (and 'undefined's for the rgb value response)
        if rgb_values:
            red = rgb_values['red']
            green = rgb_values['green']
            blue = rgb_values['blue']
            return (red, green, blue)
        else:
            return (0, 0, 0)

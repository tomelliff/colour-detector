#!/usr/bin/env python
from __future__ import division

import argparse
import base64

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

"""
Detects dominant colour in an image using Google's Vision API.
Based largely around https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/vision/api/label/label.py

Usage: ./colour_detector.py [image]
"""

def rgb(photo_file):
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
        return rgb_values

def convert_rgb_to_xyz(rgb):
    """
    Convert RGB values to XYZ values.

    Math from http://www.easyrgb.com/index.php?X=MATH&H=02#text2
    Pseudo code:

    var_R = ( R / 255 )        //R from 0 to 255
    var_G = ( G / 255 )        //G from 0 to 255
    var_B = ( B / 255 )        //B from 0 to 255

    if ( var_R > 0.04045 ) var_R = ( ( var_R + 0.055 ) / 1.055 ) ^ 2.4
    else                   var_R = var_R / 12.92
    if ( var_G > 0.04045 ) var_G = ( ( var_G + 0.055 ) / 1.055 ) ^ 2.4
    else                   var_G = var_G / 12.92
    if ( var_B > 0.04045 ) var_B = ( ( var_B + 0.055 ) / 1.055 ) ^ 2.4
    else                   var_B = var_B / 12.92

    var_R = var_R * 100
    var_G = var_G * 100
    var_B = var_B * 100

    //Observer. = 2 degrees, Illuminant = D65
    X = var_R * 0.4124 + var_G * 0.3576 + var_B * 0.1805
    Y = var_R * 0.2126 + var_G * 0.7152 + var_B * 0.0722
    Z = var_R * 0.0193 + var_G * 0.1192 + var_B * 0.9505
    """

    r = rgb['red']
    g = rgb['green']
    b = rgb['blue']

    var_r = r / 255
    var_g = g / 255
    var_b = b / 255

    if var_r > 0.04045:
        var_r = ((var_r + 0.055) / 1.055) ** 2.4
    else:
        var_r /= 12.92

    if var_g > 0.04045:
        var_g = ((var_g + 0.055) / 1.055) ** 2.4
    else:
        var_g /= 12.92

    if var_b > 0.04045:
        var_b = ((var_b + 0.055) / 1.055) ** 2.4
    else:
        var_b /= 12.92

    var_r *= 100
    var_g *= 100
    var_b *= 100

    X = var_r * 0.4124 + var_g * 0.3576 + var_b * 0.1805
    Y = var_r * 0.2126 + var_g * 0.7152 + var_b * 0.0722
    Z = var_r * 0.0193 + var_g * 0.1192 + var_b * 0.9505

    xyz = {'X': X, 'Y': Y,'Z': Z}

    print('RGB values of %s convert to XYZ values of %s' % (rgb, xyz))
    return xyz


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image_file', help='The image you\'d like to get the colour for.')
    args = parser.parse_args()
    rgb_values = rgb(args.image_file)
    convert_rgb_to_xyz(rgb_values)

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

    r /= 255
    g /= 255
    b /= 255

    if r > 0.04045:
        r = ((r + 0.055) / 1.055) ** 2.4
    else:
        r /= 12.92

    if g > 0.04045:
        g = ((g + 0.055) / 1.055) ** 2.4
    else:
        g /= 12.92

    if b > 0.04045:
        b = ((b + 0.055) / 1.055) ** 2.4
    else:
        b /= 12.92

    r *= 100
    g *= 100
    b *= 100

    x = r * 0.4124 + g * 0.3576 + b * 0.1805
    y = r * 0.2126 + g * 0.7152 + b * 0.0722
    z = r * 0.0193 + g * 0.1192 + b * 0.9505

    xyz = {'X': x, 'Y': y,'Z': z}

    print('RGB values of %s convert to XYZ values of %s' % (rgb, xyz))
    return xyz

def convert_xyz_to_cielab(xyz):
    """
    Convert RGB values to XYZ values.

    Math from http://www.easyrgb.com/index.php?X=MATH&H=07#text7
    Pseudo code:

    Observer= 2 degrees, Illuminant= D65
    var_X = X / ref_X          //ref_X =  95.047
    var_Y = Y / ref_Y          //ref_Y = 100.000
    var_Z = Z / ref_Z          //ref_Z = 108.883

    if ( var_X > 0.008856 ) var_X = var_X ^ ( 1/3 )
    else                    var_X = ( 7.787 * var_X ) + ( 16 / 116 )
    if ( var_Y > 0.008856 ) var_Y = var_Y ^ ( 1/3 )
    else                    var_Y = ( 7.787 * var_Y ) + ( 16 / 116 )
    if ( var_Z > 0.008856 ) var_Z = var_Z ^ ( 1/3 )
    else                    var_Z = ( 7.787 * var_Z ) + ( 16 / 116 )

    CIE-L* = ( 116 * var_Y ) - 16
    CIE-a* = 500 * ( var_X - var_Y )
    CIE-b* = 200 * ( var_Y - var_Z )
    """

    x = xyz['X']
    y = xyz['Y']
    z = xyz['Z']

    ref_x = 95.047
    ref_y = 100.000
    ref_z = 108.83

    x /= ref_x
    y /= ref_y
    z /= ref_z

    if x > 0.08856:
        x **= (1 / 3)
    else:
        x = (7.787 * x ) + (16 / 116)

    if y > 0.08856:
        y **= (1 / 3)
    else:
        y = (7.787 * y ) + (16 / 116)

    if z > 0.08856:
        z **= (1 / 3)
    else:
        z = (7.787 * z ) + (16 / 116)

    l = (116 * y) - 16
    a = 500 * (x - y)
    b = 200 * (y - z)

    lab = {'CIE-L*': l, 'CIE-a*': a,'CIE-b*': b}

    print('XYZ values of %s convert to CIE-L*ab values of %s' % (xyz, lab))
    return lab


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image_file', help='The image you\'d like to get the colour for.')
    args = parser.parse_args()
    rgb_values = rgb(args.image_file)
    xyz_values = convert_rgb_to_xyz(rgb_values)
    lab_values = convert_xyz_to_cielab(xyz_values)

#!/usr/bin/env python
import argparse
import base64

def process_image(image_file):
    with open(image_file, 'rb') as image:
        image_content = base64.b64encode(image.read())
        return image_content

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image_file', help='The image you\'d like to get the product code for.')
    args = parser.parse_args()

    print(process_image(args.image_file))

#!/usr/bin/env python
'''
Command line script for retrieving a product code for an exact match of the
dominant colours in the image.
'''
import argparse
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../lib/"))
import colour_detector
import data_storage
from process_image import process_image

def main(image_file, local, region):
    cd = colour_detector.ColourDetector()
    image_content = process_image(image_file)
    rgb = cd.get_rgb_values(image_content)

    ds = data_storage.DataStorage(local=local, region=region)
    print(ds.get_product_for_rgb(rgb))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image_file', help='The image you\'d like to get the product code for.')
    parser.add_argument('--region', help='AWS Region to use', dest='region')
    parser.add_argument('--local', help='Store data in a local DynamoDB instance', dest='local', action='store_true')
    parser.set_defaults(local=False)
    args = parser.parse_args()

    main(args.image_file, args.local, args.region)

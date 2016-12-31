#!/usr/bin/env python
'''
Command line script for taking an image and its associated product code
and uploading to the database.
'''
import argparse

import colour_detector
import data_storage
from process_image import process_image

def main(image_file, product_code):
    cd = colour_detector.ColourDetector()
    image_content = process_image(image_file)
    rgb = cd.get_rgb_values(image_content)

    ds = data_storage.DataStorage()
    ds.store_product_for_rgb(rgb, product_code)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image_file', help='The image you\'d like to get the colour for.')
    parser.add_argument('product_code', help='The product code for the product')
    args = parser.parse_args()

    main(args.image_file, args.product_code)

#!/usr/bin/env python
import argparse

import colour_detector
import data_storage

def main(image_file, product_code):
    cd = colour_detector.ColourDetector()
    rgb = cd.get_rgb_values(image_file)

    ds = data_storage.DataStorage()
    ds.store_rgb_for_product(rgb, product_code)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image_file', help='The image you\'d like to get the colour for.')
    parser.add_argument('product_code', help='The product code for the product')
    args = parser.parse_args()

    main(args.image_file, args.product_code)

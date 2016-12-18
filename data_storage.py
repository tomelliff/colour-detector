#!/usr/bin/env python
import argparse

import colour_detector

def _format_rgb_values(rgb_values):
    for rgb_value in rgb_values:
        return ''.join([_zero_pad_number(v) for v in rgb_values])

def _zero_pad_number(number, length=3):
    return str(number).zfill(length)

def store_rgbs_for_product(rgb, product_code):
    """
    Store the RGB values against the product code.
    For now this is just a flat CSV file.
    """

    rgb_values = _format_rgb_values(rgb)
    with open('database.txt', 'a') as database:
        database.write('{},{}\n'.format(rgb_values, product_code))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image_file', help='The image you\'d like to get the colour for.')
    parser.add_argument('product_code', help='The product code for the product')
    args = parser.parse_args()

    cd = colour_detector.ColourDetector()
    rgb = cd.get_rgb_values(args.image_file)

    store_rgbs_for_product(rgb, args.product_code)

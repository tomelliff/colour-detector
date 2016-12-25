#!/usr/bin/env python
from ast import literal_eval

import argparse

import colour_comparison
import colour_detector
import data_storage

def main(image_file):
    cd = colour_detector.ColourDetector()
    rgb = cd.get_rgb_values(image_file)
    print(rgb)

    ds = data_storage.DataStorage()
    all_products = ds.get_all_product_rgb_values()
    print(all_products)

    cc = colour_comparison.ColourComparison()
    results = []
    for product in all_products:
        print(product)
        results.append(tuple([product[1]] + cc.compare_colours(rgb, literal_eval(product[0]))))

    print(results)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image_file', help='The image you\'d like to get the colour for.')
    args = parser.parse_args()

    main(args.image_file)

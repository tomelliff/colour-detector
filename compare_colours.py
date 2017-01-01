#!/usr/bin/env python
import argparse

import colour_comparison
import colour_detector
import data_storage
from process_image import process_image

def main(image_file, local, region):
    cd = colour_detector.ColourDetector()
    image_content = process_image(image_file)
    rgb = cd.get_rgb_values(image_content)
    print(rgb)

    ds = data_storage.DataStorage(local=local, region=region)
    all_products = ds.get_all_rgb_values()
    print(all_products)

    cc = colour_comparison.ColourComparison()
    results = []
    for product in all_products:
        print(product)
        delta = cc.compare_colours(rgb, product)
        print(delta)
        results.append({round(delta, 3): rgb})

    print(results)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image_file', help='The image you\'d like to get the colour for.')
    parser.add_argument('--region', help='AWS Region to use', dest='region')
    parser.add_argument('--local', help='Store data in a local DynamoDB instance', dest='local', action='store_true')
    parser.set_defaults(local=False)
    args = parser.parse_args()

    main(args.image_file, args.local, args.region)

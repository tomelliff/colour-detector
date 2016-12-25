#!/usr/bin/env python
import argparse

import colour_detector
import data_storage

def main(image_file):
    cd = colour_detector.ColourDetector()
    rgb = cd.get_rgb_values(image_file)

    ds = data_storage.DataStorage()
    print(ds.get_product_for_rgb(rgb))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image_file', help='The image you\'d like to get the colour for.')
    args = parser.parse_args()

    main(args.image_file)

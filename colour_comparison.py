#!/usr/bin/env python

from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000

def _convert_rgb_to_lab(rgb_tuple):
    """Takes a tuple of RGB values and converts into CIELAB colour space"""

    rgb = sRGBColor(*rgb_tuple, is_upscaled=True)
    lab = convert_color(rgb, LabColor)

    return lab

def compare_colours(rgb1, rgb2):
    """Compares two RGB tuples"""

    lab1 = _convert_rgb_to_lab(rgb1)
    lab2 = _convert_rgb_to_lab(rgb2)

    delta_e = delta_e_cie2000(lab1, lab2)

    return delta_e


if __name__ == '__main__':
    mulberry_burst = (106, 82, 96)
    near_mulberry_burst = (106, 82, 95)
    off_mulberry_burst = (140, 82, 96)

    print(compare_colours(mulberry_burst, off_mulberry_burst))

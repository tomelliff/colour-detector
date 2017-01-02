import os
import sys

here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "../vendored"))

from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000

class ColourComparison(object):
    """Compares RGB colours"""

    def _convert_rgb_to_lab(self, rgb_tuple):
        """Takes a tuple of RGB values and converts into CIELAB colour space"""

        rgb = sRGBColor(*rgb_tuple, is_upscaled=True)
        lab = convert_color(rgb, LabColor)

        return lab

    def compare_colours(self, rgb1, rgb2):
        """Compares two RGB tuples"""

        lab1 = self._convert_rgb_to_lab(rgb1)
        lab2 = self._convert_rgb_to_lab(rgb2)

        delta_e = delta_e_cie2000(lab1, lab2)

        return delta_e

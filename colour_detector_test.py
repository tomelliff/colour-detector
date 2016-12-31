#!/usr/bin/env python

import unittest

from colour_detector import ColourDetector

class ColourDetectorTest(unittest.TestCase):
    def setUp(self):
        self.cd = ColourDetector()

    def test_white(self):
        white_b64 = 'iVBORw0KGgoAAAANSUhEUgAAAeAAAAHgAgMAAAAAulYGAAAADFBMVEX' \
                    '///8AAADc2c////83BRtzAAAA8klEQVR4nO3NMREAIAwEsDrAB8o51O' \
                    'EAJjT80MRAaodUv3hVxOwYjxtwxGKxWCwWi8VisVgsFovFYrFYLBaLx' \
                    'WKxWCwWi8VisVgsFovFYrFYLBaLxWKxWCwWi8VisVgsFovFYrFYLBaL' \
                    'xWKxWCwWi8VisVgsFovFYrFYLBaLxWKxWCwWi8VisVgsFovFYrFYLBa' \
                    'LxWKxWCwWi8VisVgsFovFYrFYLBaLxWKxWCwWi8VisVgsFovFYrFYLB' \
                    'aLxWKxWCwWi8VisVgsFovFYrFYLBaLxWKxWCwWi8VisVgsFovFYrFYL' \
                    'BaLxWLxjyuiY7xD+sUPl1d9uWzK18sAAAAASUVORK5CYII='
        self.assertEqual(self.cd.get_rgb_values(white_b64), (255, 255, 255))

    def test_black(self):
        black_b64 = 'iVBORw0KGgoAAAANSUhEUgAAAeAAAAHgAgMAAAAAulYGAAAADFBMVEX' \
                    '///8AAADc2c8AAAA3uz1hAAAA8klEQVR4nO3NMREAIAwEsDrAB8o51O' \
                    'EAJjT80MRAaodUv3hVxOwYjxtwxGKxWCwWi8VisVgsFovFYrFYLBaLx' \
                    'WKxWCwWi8VisVgsFovFYrFYLBaLxWKxWCwWi8VisVgsFovFYrFYLBaL' \
                    'xWKxWCwWi8VisVgsFovFYrFYLBaLxWKxWCwWi8VisVgsFovFYrFYLBa' \
                    'LxWKxWCwWi8VisVgsFovFYrFYLBaLxWKxWCwWi8VisVgsFovFYrFYLB' \
                    'aLxWKxWCwWi8VisVgsFovFYrFYLBaLxWKxWCwWi8VisVgsFovFYrFYL' \
                    'BaLxWLxjyuiY7xD+sUPl1d9uWzK18sAAAAASUVORK5CYII='
        self.assertEqual(self.cd.get_rgb_values(black_b64), (0, 0, 0))

if __name__ == '__main__':
    unittest.main()

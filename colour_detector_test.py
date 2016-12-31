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

    def test_red(self):
        red_b64 = 'iVBORw0KGgoAAAANSUhEUgAAAeAAAAHgAgMAAAAAulYGAAAADFBMVEX//' \
                  '/8AAADc2c//AACJIwmMAAAA8klEQVR4nO3NMREAIAwEsDrAB8o51OEAJj' \
                  'T80MRAaodUv3hVxOwYjxtwxGKxWCwWi8VisVgsFovFYrFYLBaLxWKxWCw' \
                  'Wi8VisVgsFovFYrFYLBaLxWKxWCwWi8VisVgsFovFYrFYLBaLxWKxWCwW' \
                  'i8VisVgsFovFYrFYLBaLxWKxWCwWi8VisVgsFovFYrFYLBaLxWKxWCwWi' \
                  '8VisVgsFovFYrFYLBaLxWKxWCwWi8VisVgsFovFYrFYLBaLxWKxWCwWi8' \
                  'VisVgsFovFYrFYLBaLxWKxWCwWi8VisVgsFovFYrFYLBaLxWLxjyuiY7x' \
                  'D+sUPl1d9uWzK18sAAAAASUVORK5CYII='
        self.assertEqual(self.cd.get_rgb_values(red_b64), (255, 0, 0))

    def test_green(self):
        green_b64 = 'iVBORw0KGgoAAAANSUhEUgAAAeAAAAHgAgMAAAAAulYGAAAADFBMVEX' \
                    '///8AAADc2c8A/wCkn8ATAAAA8klEQVR4nO3NMREAIAwEsDrAB8o51O' \
                    'EAJjT80MRAaodUv3hVxOwYjxtwxGKxWCwWi8VisVgsFovFYrFYLBaLx' \
                    'WKxWCwWi8VisVgsFovFYrFYLBaLxWKxWCwWi8VisVgsFovFYrFYLBaL' \
                    'xWKxWCwWi8VisVgsFovFYrFYLBaLxWKxWCwWi8VisVgsFovFYrFYLBa' \
                    'LxWKxWCwWi8VisVgsFovFYrFYLBaLxWKxWCwWi8VisVgsFovFYrFYLB' \
                    'aLxWKxWCwWi8VisVgsFovFYrFYLBaLxWKxWCwWi8VisVgsFovFYrFYL' \
                    'BaLxWLxjyuiY7xD+sUPl1d9uWzK18sAAAAASUVORK5CYII='
        self.assertEqual(self.cd.get_rgb_values(green_b64), (0, 255, 0))

    def test_blue(self):
        blue_b64 = 'iVBORw0KGgoAAAANSUhEUgAAAeAAAAHgAgMAAAAAulYGAAAADFBMVEX/' \
                   '//8AAADc2c8AAP8audLsAAAA8klEQVR4nO3NMREAIAwEsDrAB8o51OEA' \
                   'JjT80MRAaodUv3hVxOwYjxtwxGKxWCwWi8VisVgsFovFYrFYLBaLxWKx' \
                   'WCwWi8VisVgsFovFYrFYLBaLxWKxWCwWi8VisVgsFovFYrFYLBaLxWKx' \
                   'WCwWi8VisVgsFovFYrFYLBaLxWKxWCwWi8VisVgsFovFYrFYLBaLxWKx' \
                   'WCwWi8VisVgsFovFYrFYLBaLxWKxWCwWi8VisVgsFovFYrFYLBaLxWKx' \
                   'WCwWi8VisVgsFovFYrFYLBaLxWKxWCwWi8VisVgsFovFYrFYLBaLxWLx' \
                   'jyuiY7xD+sUPl1d9uWzK18sAAAAASUVORK5CYII='
        self.assertEqual(self.cd.get_rgb_values(blue_b64), (0, 0, 255))

if __name__ == '__main__':
    unittest.main()

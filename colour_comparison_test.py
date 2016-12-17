#!/usr/bin/env python

import unittest

from colour_comparison import ColourComparison

class ColourComparisonTest(unittest.TestCase):
    white = (255, 255, 255)
    black = (0, 0, 0)
    mulberry_burst = (106, 82, 96)
    near_mulberry_burst = (106, 82, 95)
    off_mulberry_burst = (140, 82, 96)

    def setUp(self):
        self.cc = ColourComparison()

    def test_compare_white_to_white(self):
        self.assertEqual(self.cc.compare_colours(self.white, self.white), 0)

    def test_compare_black_to_black(self):
        self.assertEqual(self.cc.compare_colours(self.black, self.black), 0)

    def test_compare_black_to_white(self):
        self.assertAlmostEqual(self.cc.compare_colours(self.white, self.black), 100, places=4)

    def test_compare_mulberry_burst_to_off_mulberry_burst(self):
        self.assertEqual(self.cc.compare_colours(self.off_mulberry_burst, self.mulberry_burst), 10.137177399844706)

    def test_compare_mulberry_burst_to_near_mulberry_burst(self):
        self.assertEqual(self.cc.compare_colours(self.near_mulberry_burst, self.mulberry_burst), 0.4197581985580754)


if __name__ == '__main__':
    unittest.main()

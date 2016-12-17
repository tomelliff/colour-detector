#!/usr/bin/env python
from __future__ import division

from math import sqrt

def compare_colours(colour1, colour2):
    """
    Compares two colours using Delta E 1994 comparison.
    Takes two colours' CIE-L*ab values as dictionaries.

    Math from http://www.easyrgb.com/index.php?X=DELT&H=04#text4
    Pseudo code:

    CIE-L*1, CIE-a*1, CIE-b*1          //Color #1 CIE-L*ab values
    CIE-L*2, CIE-a*2, CIE-b*2          //Color #2 CIE-L*ab values
    WHT-L, WHT-C, WHT-H                //Weighting factors depending
                                       //on the application (1 = default)

    xC1 = sqrt( ( CIE-a*1 ^ 2 ) + ( CIE-b*1 ^ 2 ) )
    xC2 = sqrt( ( CIE-a*2 ^ 2 ) + ( CIE-b*2 ^ 2 ) )
    xDL = CIE-L*2 - CIE-L*1
    xDC = xC2 - xC1
    xDE = sqrt( ( ( CIE-L*1 - CIE-L*2 ) * ( CIE-L*1 - CIE-L*2 ) )
              + ( ( CIE-a*1 - CIE-a*2 ) * ( CIE-a*1 - CIE-a*2 ) )
              + ( ( CIE-b*1 - CIE-b*2 ) * ( CIE-b*1 - CIE-b*2 ) ) )
    if ( sqrt( xDE ) > ( sqrt( abs( xDL ) ) + sqrt( abs( xDC ) ) ) ) {
       xDH = sqrt( ( xDE * xDE ) - ( xDL * xDL ) - ( xDC * xDC ) )
    }
    else {
       xDH = 0
    }
    xSC = 1 + ( 0.045 * xC1 )
    xSH = 1 + ( 0.015 * xC1 )
    xDL /= WHT-L
    xDC /= WHT-C * xSC
    xDH /= WHT-H * xSH
    Delta E94 = sqrt( xDL ^ 2 + xDC ^ 2 + xDH ^ 2 )
    """

    l1 = colour1['CIE-L*']
    a1 = colour1['CIE-a*']
    b1 = colour1['CIE-b*']

    l2 = colour2['CIE-L*']
    a2 = colour2['CIE-a*']
    b2 = colour2['CIE-b*']

    whtl = 1
    whtc = 1
    whth = 1

    xc1 = sqrt((a1 ** 2) + (b1 ** 2))
    xc2 = sqrt((a2 ** 2) + (b2 ** 2))
    xdl = l2 - l1
    xdc = xc2 - xc1
    xde = sqrt( ((l1 - l2) ** 2)
              + ((a1 - a2) ** 2)
              + ((b1 - b2) ** 2) )

    if (sqrt(xde) > (sqrt(abs(xdl)) + sqrt(abs(xdc)))):
        xdh = sqrt((xde ** 2) - (xdl ** 2) - (xdc ** 2))
    else:
        xdh = 0

    xsc = 1 + (0.045 * xc1)
    xsh = 1 + (0.015 * xc1)
    xdl /= whtl
    xdc /= (whtc * xsc)
    xdh /= (whth * xsh)

    delta_e94 = sqrt(xdl ** 2 + xdc ** 2 + xdh ** 2)

    print('The Delta E94 comparison of %s and %s is %s' % (colour1, colour2, delta_e94))
    return delta_e94

if __name__ == '__main__':
    white = {'CIE-b*': -0.010, 'CIE-a*': 0.005, 'CIE-L*': 100.000}
    black = {'CIE-b*': 0, 'CIE-a*': 0, 'CIE-L*': 0}
    mulberry_burst = {'CIE-b*': -4.308149163408482, 'CIE-a*': 12.556231265920037, 'CIE-L*': 37.740450406310735}
    off_mulberry_burst = {'CIE-b*': 2.340, 'CIE-a*': 26.057, 'CIE-L*': 41.930}
    near_mulberry_burst = {'CIE-b*': -4.308149163408482, 'CIE-a*': 12.556231265920037, 'CIE-L*': 37.740450406310735}

    colour1 = mulberry_burst
    colour2 = off_mulberry_burst
    compare_colours(colour1, colour2)

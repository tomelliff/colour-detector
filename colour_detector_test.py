import colour_detector

def test_convert_rgb_to_xyz():
    mulberry_burst_rgb = {'red': 106, 'green': 82, 'blue': 96}
    mulberry_burst_xyz = {'Y': 9.94328616129628, 'X': 11.072472016046184, 'Z': 12.401994360808763}
    assert colour_detector.convert_rgb_to_xyz(mulberry_burst_rgb) == mulberry_burst_xyz

def test_convert_xyz_to_cielab():
    mulberry_burst_xyz = {'Y': 9.94328616129628, 'X': 11.072472016046184, 'Z': 12.401994360808763}
    mulberry_burst_cielab = {'CIE-b*': -4.308149163408482, 'CIE-a*': 12.556231265920037, 'CIE-L*': 37.740450406310735}
    assert colour_detector.convert_xyz_to_cielab(mulberry_burst_xyz) == mulberry_burst_cielab

test_convert_rgb_to_xyz()
test_convert_xyz_to_cielab()

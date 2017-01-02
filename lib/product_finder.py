from operator import itemgetter

import colour_comparison
import colour_detector
import data_storage

def _get_image_rgb_values(image_content):
    cd = colour_detector.ColourDetector()
    image_rgb_values = cd.get_rgb_values(image_content)
    return image_rgb_values

def _get_all_stored_rgb_values(local, region, table_name):
    ds = data_storage.DataStorage(local=local, region=region, table_name=table_name)
    all_products = ds.get_all_rgb_values()
    return all_products

def _get_product_for_rgb_values(local, region, table_name, rgb_values):
    ds = data_storage.DataStorage(local=local, region=region, table_name=table_name)
    product_code = ds.get_product_for_rgb(rgb_values)
    return product_code

def _compare_colours(uploaded_rgb, product_rgb):
    cc = colour_comparison.ColourComparison()
    delta = cc.compare_colours(uploaded_rgb, product_rgb)
    return delta

def find_product(local, region, table_name, image_content):
    image_rgb_values = _get_image_rgb_values(image_content)
    all_products = _get_all_stored_rgb_values(local, region, table_name)

    results = []
    for product in all_products:
        delta = _compare_colours(image_rgb_values, product)
        results.append({'delta': round(delta, 3), 'rgb_values': product})

    sorted_results = sorted(results, key=itemgetter('delta'))
    closest_match = sorted_results[0]
    closest_rgb = closest_match['rgb_values']
    closest_delta = closest_match['delta']

    closest_product = _get_product_for_rgb_values(local, region, table_name, closest_rgb)

    return (closest_product, closest_delta)

# base64_image = 'iVBORw0KGgoAAAANSUhEUgAAAeAAAAHgAgMAAAAAulYGAAAADFBMVEX' \
#             '///8AAADc2c////83BRtzAAAA8klEQVR4nO3NMREAIAwEsDrAB8o51O' \
#             'EAJjT80MRAaodUv3hVxOwYjxtwxGKxWCwWi8VisVgsFovFYrFYLBaLx' \
#             'WKxWCwWi8VisVgsFovFYrFYLBaLxWKxWCwWi8VisVgsFovFYrFYLBaL' \
#             'xWKxWCwWi8VisVgsFovFYrFYLBaLxWKxWCwWi8VisVgsFovFYrFYLBa' \
#             'LxWKxWCwWi8VisVgsFovFYrFYLBaLxWKxWCwWi8VisVgsFovFYrFYLB' \
#             'aLxWKxWCwWi8VisVgsFovFYrFYLBaLxWKxWCwWi8VisVgsFovFYrFYL' \
#             'BaLxWLxjyuiY7xD+sUPl1d9uWzK18sAAAAASUVORK5CYII='
# print(find_product(True, 'eu-west-1', 'ProductColours', base64_image))

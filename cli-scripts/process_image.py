import base64

def process_image(image_file):
    with open(image_file, 'rb') as image:
        image_content = base64.b64encode(image.read())
        return image_content

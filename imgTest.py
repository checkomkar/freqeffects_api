import argparse
import io

from google.cloud import vision
from google.cloud.vision import types
import json

GOOGLE_APPLICATION_CREDENTIALS = 'instabot-7bc58a069394.json'
# [START def_detect_properties_uri]
client = vision.ImageAnnotatorClient()
image = types.Image()
image.source.image_uri = 'https://upload.wikimedia.org/wikipedia/commons/d/d1/Mount_Everest_as_seen_from_Drukair2_PLW_edit.jpg'

response = client.image_properties(image=image)
props = response.image_properties_annotation
print json.dumps(props)
print('Properties:')

for color in props.dominant_colors.colors:
    print('frac: {}'.format(color.pixel_fraction))
    print('\tr: {}'.format(color.color.red))
    print('\tg: {}'.format(color.color.green))
    print('\tb: {}'.format(color.color.blue))
    print('\ta: {}'.format(color.color.alpha))
    """Detects image properties in the file located in Google Cloud Storage or
    on the Web."""

# [END def_detect_properties_uri]
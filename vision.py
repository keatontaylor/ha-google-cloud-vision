
import io
import os
import glob
filelist = glob.glob('/opt/homeassistant/mail/*.jpg')

# Imports the Google Cloud client library
from google.cloud import vision

# Instantiates a client
vision_client = vision.Client(project='mailocr')

contains_keyword = 0

keywords = ['notification', 'jury duty', 'statement', 'important']

for file in filelist:
    file_name = os.path.join(
        os.path.dirname(__file__),
        file)

    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
        image = vision_client.image(
            content=content)

    texts = image.detect_text()

    for text in texts:
        if any(word in text.description.lower() for word in keywords):
            contains_keyword = contains_keyword + 1
            break


print(contains_keyword)
import requests
from PIL import Image
from io import BytesIO


def pil_to_bytes(image):
    byteIO = BytesIO()
    image.save(byteIO, format='PNG')
    return byteIO.getvalue()


response = requests.get(
    'http://c.files.bbci.co.uk/48DD/production/_107435681_perro1.jpg'
)
imageObject = Image.open(BytesIO(response.content))
some_bytes = pil_to_bytes(imageObject)
with open("test.png", "wb") as binary_file:
    binary_file.write(some_bytes)

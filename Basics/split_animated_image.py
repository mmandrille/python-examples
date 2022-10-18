from PIL import Image
import requests
from io import BytesIO


def get_images_from_url(url):
    images = []
    response = requests.get(url)
    imageObject = Image.open(BytesIO(response.content))
    try:
        if imageObject.is_animated:
            for frame in range(0, imageObject.n_frames):
                imageObject.seek(frame)
                images.append(imageObject)

        return images

    except AttributeError:
        return [imageObject, ]


# Animated
images = get_images_from_url('https://storage.googleapis.com/infoxel-tagx-thumbs/Portales/Ads/ad_2022-10-18T14%3A00%3A30_300_600.png')
for image in images:
    image.show()

# Not animated
images = get_images_from_url('http://c.files.bbci.co.uk/48DD/production/_107435681_perro1.jpg')
for image in images:
    image.show()

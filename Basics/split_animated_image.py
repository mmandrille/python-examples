from PIL import Image
import requests
from io import BytesIO


def get_images_from_url(url):
    images = []
    response = requests.get(url)
    imageObject = Image.open(BytesIO(response.content))
    if imageObject.is_animated:
        for frame in range(0,imageObject.n_frames):
            imageObject.seek(frame)
            images.append(imageObject)

    return images


images = get_images_from_url('https://storage.googleapis.com/infoxel-tagx-thumbs/Portales/Ads/ad_2022-10-18T14%3A00%3A30_300_600.png')
for image in images:
    image.show()

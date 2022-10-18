import json
import requests
from urllib.parse import urlparse
from datetime import datetime


# Enviroment Variables
IMATCH_URL = 'http://localhost:8888'
MIN_THREASHOLD = 85


# code
class ImageMatcher():
    def __init__(self, image_url):
        self.image_url = image_url
        self.image_path = self.download_image()
        self.run()

    def download_image(self):
        img_data = requests.get(self.image_url).content
        path = 'temp/' + urlparse(self.image_url).path.replace('/', '_')
        with open(path, 'wb') as handler:
            handler.write(img_data)
        return path

    def check(self):
        response = requests.post(
            f'{IMATCH_URL}/search',
            files={'image': open(self.image_path, 'rb')}
        )
        if 'result' in response.json():
            for result in response.json()['result']:
                if result['score'] > MIN_THREASHOLD:
                    return response.json()

    def add(self):
        response = requests.post(
            f'{IMATCH_URL}/add',
            data={
                'url': self.image_url,
                'filepath': self.image_path,
                'metadata': json.dumps({
                    'url': self.image_url,
                    'path': self.image_path,
                    'created_at': datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
                })
            },
        )
        if response.status_code == 200:
            return response.json()

    def run(self):
        self.response = {}
        self.response['image_url'] = self.image_url
        self.response['image_path'] = self.image_path
        self.response['exists'] = self.check()
        if not self.response['exists']:
            self.response['created'] = self.add()
        return self.response


# Code
if __name__ == "__main__":
    url = 'https://picsum.photos/200/300'
    dinamic_url = 'https://source.unsplash.com/user/c_v_r/480x240'
    # First Time
    im = ImageMatcher(url)
    print(f"First Test: {im.response}")
    # Second Time
    im = ImageMatcher(url)
    print(f"Second Test: {im.response}")

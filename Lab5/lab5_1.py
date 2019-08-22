import os

import requests
from requests.exceptions import RequestException

base_url = 'https://unsplash.com/napi/collections/3330448/photos'
IMAGE_SRC = './imgs'


def get_one_page(offset):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Connection': 'close'
        }
        params = {
            'page': offset,
            'per_page': '10',
            'order_by': 'latest',
            'share_key': '039a27cbd24691f95ac32fe494ce28f8',
        }
        response = requests.get(base_url, headers=headers, params=params)
        response.encoding = 'utf-8'
        if response.status_code == 200:
            return response.json()
        return None
    except RequestException:
        return None


def get_image_url(jsons):
    for json in jsons:
        yield {
            'full': json['urls']['full'],
            'raw': json['urls']['raw'],
            'regular': json['urls']['regular'],
            'small': json['urls']['small'],
            'thumb': json['urls']['thumb']
        }


def save_img(image_urls, type='full'):
    for idx, image_url in enumerate(image_urls):
        link = image_url[type]
        r = requests.get(link)
        filename = IMAGE_SRC + str(idx) + '_' + type + '.jpg'
        filepath = IMAGE_SRC + "/" + filename
        try:
            if not os.path.exists(IMAGE_SRC):
                os.mkdir(IMAGE_SRC)
            with open(filepath, 'wb') as f:
                f.write(r.content)
        except IOError as e:
            print('Save Img Error', e)


def main():
    offset = 3
    response = get_one_page(offset)
    # print(json.dumps(response, sort_keys=True, indent=4, separators=(',', ': ')))
    # print(response)
    image_urls = get_image_url(response)
    # for image_url in get_image_url(response):
    #     print(image_url)
    # print(json.dumps(image_urls, sort_keys=True, indent=4, separators=(',', ': ')))
    save_img(image_urls)


if __name__ == '__main__':
    main()

import requests
from lxml import etree
from requests.exceptions import RequestException


def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Connection': 'close'
        }
        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8'
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def get_image_url(html):
    selector = etree.HTML(html)
    img = selector.xpath('/html/body/div[2]/div/div[2]/div[1]/div/div[1]/div[1]/a/img/@src')
    # print(type(str(img[0])))
    return img[0]


def save_img(url):
    r = requests.get(url)
    with open('轮到你了.jpg', 'wb') as f:
        f.write(r.content)


if __name__ == '__main__':
    url = 'https://www.rijutv.com/riju/13040.html'
    response = get_one_page(url)
    image_url = get_image_url(response)
    # print(image_url)
    save_img(image_url)
import json
import re
import time

import requests
from requests.exceptions import RequestException


def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Connection': 'close'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    selector = etree.HTML(html)
    total = selector.xpath('//*[@id="J_goodsList"]/ul/li')
    for i, item in enumerate(total):
        price = item.xpath('//div/div[2]/strong/i/text()')
        name = item.xpath('//div/div[3]/a/em/text()')
        author = item.xpath('//div[4]/span[1]/a/text()')
        press = item.xpath('//div[4]/span[2]/a/text()')
        shopname = item.xpath('//div[6]/a/text()')
        yield {
            'bookname': name[i],
            'author': author[i],
            'press': press[i],
            'price': price[i],
            'shopname': shopname[i],
        }


def write_to_file(content):
    with open('./result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(offset):
    url = 'https://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        write_to_file(item)
        print(item)


if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)
        time.sleep(1)

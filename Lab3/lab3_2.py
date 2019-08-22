# -*- coding: utf-8 -*-
import multiprocessing
import time

import requests
from lxml import etree
from requests.exceptions import RequestException

PAGE_START = 1
PAGE_END = 15
PAGE_PER_LIST = 3

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
    total = selector.xpath('//*[@id="main"]/div/div[3]/div[3]/div')
    for i, item in enumerate(total):
        idx = item.xpath('//div[2]/h3/span/text()')
        name = item.xpath('//div[2]/h3/a/text()')
        print(name)
        name[i] = name[i].replace(' ', '')
        yield {
            'index': idx[i],
            'name': name[i]
        }


def write_to_file(content, offset):
    with open('./keywords' + str(offset) + '.txt', 'a', encoding='utf-8') as f:
        f.write(content['name'])


def main(offset):
    url = 'https://www.imdb.com/list/ls066061932/?sort=list_order,asc&mode=detail&page=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        write_to_file(item, offset)
        print(item)
    time.sleep(1)


if __name__ == '__main__':
    pool = multiprocessing.Pool()
    page_num = ([x for x in range(PAGE_START, PAGE_END + 1)])
    pool.map(main, page_num)
    pool.close()
    pool.join()

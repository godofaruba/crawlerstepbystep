import json
import os
import random
import threading
import time
import urllib
from queue import Queue

import requests
from bs4 import BeautifulSoup

# 使用队列保存存放图片 url 地址, 确保线程同步
url_queue = Queue()
# 线程总数
THREAD_SUM = 5
# 存储图片的位置
IMAGE_SRC = 'D://Unsplash/'


def get_all_url():
    """ 循环计算出所有的 url 地址, 存放到队列中 """
    base_url = 'https://unsplash.com/napi/collections/1065976/photos?page={}&per_page=10&order_by=latest'
    flag = 1
    max_page = 184
    for page in range(1, max_page):
        url = base_url.format(page)
        url_queue.put(url)
        flag += 1
    print('Download for', url_queue.qsize(), 'pictures.')


def get_html(url):
    response = requests.get(url)
    # print(response.text)
    soup = BeautifulSoup(response.content, 'lxml')
    # print(soup.prettify())
    imgs = soup.find_all('img')
    for img in imgs:
        print(img)


class Unsplash(threading.Thread):
    NOT_EXIST = 0

    def __init__(self, thread_id):
        threading.Thread.__init__(self)
        self.thread_id = thread_id

    def run(self):
        while not self.NOT_EXIST:
            # 队列为空, 结束线程
            if url_queue.empty():
                NOT_EXIST = 1
                break
            url = url_queue.get()
            self.get_data(url)
            time.sleep(random.randint(3, 5))

    def get_data(self, url):
        headers = {
            'User-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.3964.2 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'referer': 'https://unsplash.com/',
            'path': url.split('com')[1],
            'authority': 'unsplash.com',
            'viewport-width': '1920',
        }
        response = requests.get(url, headers=headers)
        print('Requesting for' + url + ' ,status_code' is response.status_code)
        self.get_image_url(response.text)

    def get_image_url(self, response):
        image_url = json.loads(response)[0]['urls']['full']
        self.save_img(image_url)

    def save_img(self, image_url):
        print('线程', self.thread_id, ' | 正在下载', image_url)
        try:
            if not os.path.exists(IMAGE_SRC):
                os.mkdir(IMAGE_SRC)
            filename = IMAGE_SRC + image_url.split('com')[1].split('?')[0] + '.jpg'
            # 下载图片，并保存到文件夹中
            urllib.request.urlretrieve(image_url, filename=filename)
        except IOError as e:
            print('保存图片出现异常失败', e)


if __name__ == '__main__':
    # url = 'https://unsplash.com/t/wallpapers'
    # get_html(url)
    get_all_url()
    for i in range(THREAD_SUM):
        unsplash = Unsplash(i + 1)
        unsplash.start()

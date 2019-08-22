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
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    s = etree.HTML(html)
    film = s.xpath('//*[@id="content"]/h1/span[1]/text()')
    director = s.xpath('//*[@id="info"]/span[1]/span[2]/a/text()')
    actor = s.xpath('//*[@id="info"]/span[3]/span[2]/a/text()')
    time = s.xpath('//*[@id="info"]/span[13]/text()')
    yield {
        'moviename': film,
        'director': director,
        'actor': actor,
        'time': time
    }


def main():
    url = 'https://movie.douban.com/subject/1292052/'
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)


if __name__ == '__main__':
    main()

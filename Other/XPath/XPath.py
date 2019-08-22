import json

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


def xpath_parse_text(text):
    text_xpath = etree.HTML(text)
    result = etree.tostring(text_xpath)
    # print(result)
    print(result.decode('utf-8'))


def xpath_parse_html(htmlpath):
    html = etree.parse(htmlpath, etree.HTMLParser())
    result = html.xpath('//*')
    li = html.xpath('//li')
    li_a = html.xpath('//li/a')
    # print(result)
    print(li_a)

def write_to_file(content):
    with open('./result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main():
    text = """
        <div>
            <ul>
            <li class="item-O"><a href="linkl.html">first item</a></li>
            <li class="item-1"><a href="link2.html">second item</a></li>
            <li class="item-inactive"><a href="link3.html">third item</a></li>
            <li class="item-1"><a href="link4.html">fourth item</a></li>
            <li class="item-0"><a href="link5.html"＞fifth item</a>
            </ul>
        </div>"""
    # xpath_parse_text(text)
    xpath_parse_html('./1.html')


if __name__ == '__main__':
    main()

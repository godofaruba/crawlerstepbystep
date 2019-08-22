import requests


def get_image_url(url):
    r = requests.get(url)
    with open('favicon.ico', 'wb') as f:
        f.write(r.content)


if __name__ == '__main__':
    url = 'https://github.com/favicon.ico'
    get_image_url(url)

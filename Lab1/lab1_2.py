import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Connection': 'close'
}
try:
    response = requests.get('https://www.zhihu.com/', headers=headers)
except requests.exceptions.ConnectionError:
    response.status_code = "Connection refused"

print(type(response.url), response.url)
print(type(response), response.content)
print(type(response.status_code), response.status_code)
print(type(response.text), response.text)
print(type(response.cookies), response.cookies)

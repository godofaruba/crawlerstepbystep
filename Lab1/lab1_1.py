import requests

try:
    response = requests.get('https://channel.jd.com/1713-3259.html')
except requests.exceptions.ConnectionError:
    response.status_code = "Connection refused"

print(type(response.url), response.url)
print(type(response), response.content)
print(type(response.status_code), response.status_code)
print(type(response.text), response.text)
print(type(response.cookies), response.cookies)

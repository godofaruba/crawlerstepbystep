import urllib.error
import urllib.request

url = "http://www.baidu.com"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)
try:
    response = urllib.request.urlopen(request)
except urllib.error.HTTPError as e:
    print('code: ' + e.code + '\n')
    print('reason: ' + e.reason + '\n')
    print('headers: ' + e.headers + '\n')
except urllib.error.URLError as e:
    print(e.reason)

html = response.read()  # 获取到页面的源代码
# print(html.decode('utf-8'))  # 转化为 utf-8 编码
print(response.getcode())
print(response.geturl())
# print(response.info())

fhandle = open("./1.html", "wb")
fhandle.write(html)

fhandle.close()

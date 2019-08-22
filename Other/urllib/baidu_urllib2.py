import socket
import urllib.error
import urllib.request

from bs4 import BeautifulSoup

url = "http://www.baidu.com"
# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

# ---------- 请求 ----------- #
# 构造 Resquest 请求
request = urllib.request.Request(url=url, headers=headers)
try:
    # 使用 urlopen 访问
    response = urllib.request.urlopen(request, timeout=5)

# ---------- 异常处理 ----------- #
except urllib.error.HTTPError as e:
    print('code: ' + e.code + '\n')
    print('reason: ' + e.reason + '\n')
    print('headers: ' + e.headers + '\n')
except urllib.error.URLError as e:
    print(e.reason)
    if isinstance(e.reason, socket.timeout):
        print("Time out!")
else:
    print("Request Successfully!")

# ---------- 状态码、响应头 ----------- #
print(response.getcode())
print(response.geturl())
print(type(response))
print(response.status)
print(response.getheaders())
print(response.getheader('Set-Cookie'))
# print(response.info())

# ---------- 页面解析 ----------- #
bsObj = BeautifulSoup(response.read(), features="lxml")
print(bsObj.prettify())

# ---------- 输出结果 ----------- #
html = response.read()  # 获取到页面的源代码
# print(html.decode('utf-8'))  # 转化为 utf-8 编码

# ---------- 写入文件 ----------- #
# fhandle = open("./1.html", "wb")
# fhandle.write(html)
# fhandle.close()

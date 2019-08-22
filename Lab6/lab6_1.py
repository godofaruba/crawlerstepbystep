import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('http://www.google.com')
# print(browser.page_source)
input = browser.find_element_by_name('q')
# print(input)
input.send_keys('hello world')
time.sleep(1)
input.clear()
input.send_keys('Unsplash')
input.send_keys(Keys.ENTER)
browser.close()

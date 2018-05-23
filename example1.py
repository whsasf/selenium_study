#!/usr/bin/env python3
# coding=utf-8  

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()

browser.get('https://www.baidu.com')
assert '百度一下，你就知道' in browser.title

elem = browser.find_element_by_name('wd')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)
time.sleep(2)
browser.back()
time.sleep(2)
browser.forward()
time.sleep(2)
browser.quit()
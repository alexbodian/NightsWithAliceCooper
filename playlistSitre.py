'''
Program gets the playlist from nightswithalicecooper




'''

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
# from __future__ import unicode_literals
import io
from bs4 import BeautifulSoup
import urllib
from selenium import webdriver

from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.playlist-converter.net/#/")

# driver.switch_to("tab-content")
dr = driver.find_element_by_name('text')
dr.click()

dr.send_keys('kek')
dr.send_keys('/n')
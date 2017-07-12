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

# ENTER makes it so that new line is made when called

# textBody = ''

# dr.send_keys(textBody)
# dr.send_keys(Keys.SHIFT, Keys.ENTER)


# opening the file for pasting
f1 = open('aliceCooper.txt', 'r')

for line in open('aliceCooper.txt'):

    dr.send_keys(f1.readline())
    dr.send_keys(Keys.SHIFT, Keys.ENTER)


#  submits the playlist text that was entered into the textbox
submit = driver.find_element_by_name('importtxtfreetext')
submit.click()
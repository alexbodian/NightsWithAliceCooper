'''
Test program for creating a url using a playlist txt file

Jane - Jefferson Starship
Jane%20-%20Jefferson%20Starship

(5/23)

Idea/Goal:
Create a program that converts the
AliceCooper text doc playlist into another
text doc that only contains a list of the urls for each daily playlist

The first test case for the instance of one song correctly
launches the webpage with proper formtting

Proper formatting for the prefix for a prlaylist url
as well as the example of a song and artist for the playlist:

urlbeginning = 'http://www.playlist-converter.net/#/freetext='
songString = 'Jane%20-%20Jefferson%20Starship'

'''

import sys
import  webbrowser

reload(sys)
sys.setdefaultencoding('utf-8')
# from __future__ import unicode_literals
import io
from bs4 import BeautifulSoup
import urllib
import sys

urlbeginning = 'http://www.playlist-converter.net/#/freetext='
songString = 'Jane%20-%20Jefferson%20Starship'

# finalURL = urlbeginning + songString
# webbrowser.open(finalURL)

f = open('aliceCooper.txt', 'r')

line = f.readline()

while(line != ''):
    




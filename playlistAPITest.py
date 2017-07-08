# coding: utf-8

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

Not sure if what's being printed out in the console actually has new lines separting 
each line or if thats the way that it's just being displayed in the console
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

f = open('playlisturl.txt', 'w')
urlbeginning = 'http://www.playlist-converter.net/#/freetext='
# songString = 'Jane%20-%20Jefferson%20Starship'
#
# finalURL = urlbeginning + songString

f1 = open('aliceCooper.txt', 'r')

i = 0


for line in open('aliceCooper.txt'):
    line = f1.readline()

    if (line != '\n') and i != 0:
        urlbeginning += line.replace( ' ', "%20")
        urlbeginning.replace('–', '-')
        urlbeginning += '%0A'

    if line == '':
        break;
    i+=1

print (urlbeginning)
f.write(urlbeginning)
webbrowser.open(urlbeginning)




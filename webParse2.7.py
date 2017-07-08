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

string = 'http://www.nightswithalicecooper.com/on-the-air/last-nights-music/page/'
temp = string
j = input('Enter the number of nights of songs you want: ')
j += 1

f = open('aliceCooper.txt', 'w')
k = 1

l = input('Enter the number of nights ago from now that you want listed: ')
l += 1

for i in range(l, j):
    temp = string + str(i)
    # print string
    r = urllib.urlopen(temp).read()
    soup = BeautifulSoup(r, "html.parser")

    title = soup.find_all("h1", class_="entry-title")

    content = soup.find_all("div", class_="entry-content")

    # print type(title)

    # prints title of page, date is the title
    f.write('Nights With Alice Cooper ')
    t = str(title[0].text)
    f.write(t)
    f.write('\n')

    # print title[0].text



    c = str(content[0].text)
    f.write(c)
    f.write('\n')
    f.write('\n')

    # print content[0].text



    temp = string
    print ('Night ' + str(k) + ' done.')
    k += 1

f.close()
print '\n'
print 'DONE'

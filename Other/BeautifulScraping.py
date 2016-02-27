import urllib
import re
from BeautifulSoup import *

urll = 'http://python-data.dr-chuck.net/comments_42.html'
html = urllib.urlopen(urll).read()
soup = BeautifulSoup(html)
tags = soup('span')
i = 0
for  tag in tags:
    print tag
print i
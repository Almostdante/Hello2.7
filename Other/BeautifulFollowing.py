
import urllib
import re
from bs4 import *

urll = raw_input('Enter URL') # лпвжылвтпыж
count = int(raw_input('Enter count'))
position = int(raw_input('Enter position'))

while count > 0:
    tags = BeautifulSoup(urllib.urlopen(urll).read(), "html.parser")('a')
    name = re.findall ('([a-zA-Z]+)</a>',str(tags[position-1]))[0]
    urll = tags[position-1].get('href', None)
    count = count - 1
print name
import BeautifulSoup
import urllib2
import re
import datetime
import imdb_api

url = 'http://nnm-club.me/forum/tracker.php?f=954,885,912,227,661,218'
headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.151 Safari/535.19' }
req = urllib2.Request(url, '', headers)
urll = urllib2.urlopen(req).read()
soup = BeautifulSoup.BeautifulSoup(urll)
a = soup.findAll('tr', {'class': 'prow1'})
a+= soup.findAll('tr', {'class': 'prow2'})
final = {}
for x in a:
    z = re.findall('([0-9\-]+2016)<\/td>', str(x))
    zz = z[0].split('-')
    diff = datetime.date.today() - datetime.date(int(zz[2]),int(zz[1]),int(zz[0]))
    if diff.days > 2:
        print 'tiiiime'
        continue
    y = re.findall('<a.+genmed topic.+\/(.+?\([0-9]+\))', str(x))
    if y:
       n = y[0].split('(')
       final[n[0].strip()] = n[1][:-1]
print final
for x in final:
    print x, final[x]
    try:
        print imdb_api.IMDB_Search(x, final[x])
    except:
        print 'sorry'
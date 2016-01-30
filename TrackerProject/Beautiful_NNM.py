          # This Python file uses the following encoding: utf-8

import BeautifulSoup
import urllib2
import re
import datetime

url = 'http://nnm-club.me/forum/tracker.php?f=954,885,912,227,661,218'
def parse_nnm():
    counter = open('counter', 'r')
    int_max = int(counter.readline())
    counter.close()
    headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.151 Safari/535.19' }
    req = urllib2.Request(url, '', headers)
    urll = urllib2.urlopen(req).read()
    soup = BeautifulSoup.BeautifulSoup(urll)
    a = soup.findAll('tr', {'class': 'prow1'})
    a+= soup.findAll('tr', {'class': 'prow2'})
    result = {}
    for x in a:
        z = re.findall('([0-9\-]+2016)<\/td>', str(x))
        zz = z[0].split('-')
        y = re.findall('<a.+genmed topic.+\/(.+?\([0-9]+\))', str(x))
        count = re.findall('viewtopic.+?([0-9]+)', str(x))
        if int(count[0]) > int_max:
            int_max = int(count[0])
            counter = open('counter', 'w')
            counter.write(str(int_max))
            counter.close()
        if y:
            n = y[0].split('(')
            result[n[0].strip()] = n[1][:-1]
    return result


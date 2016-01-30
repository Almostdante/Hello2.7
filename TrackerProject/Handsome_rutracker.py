          # This Python file uses the following encoding: utf-8

import BeautifulSoup
import urllib2
import re
import cookielib
from urllib import urlencode, quote, unquote
from urllib2 import build_opener, HTTPCookieProcessor

credentials = {'login_username': u'cheshiremajor', 'login_password': u'ZNt,zK.,k.', 'login': u'Вход',}
login_url = 'http://login.rutracker.org/forum/login.php'
search_url = 'http://rutracker.org/forum/tracker.php?f=2198,2199,2201,2339,312,313'


def dict_encode(dict, encoding='cp1251'):
    """Encode dict values to encoding (default: cp1251)."""
    encoded_dict = {}
    for key in dict:
        encoded_dict[key] = dict[key].encode(encoding)
    return encoded_dict

def parse_rutr():
    counter = open('counter_rutr', 'r')
    categories_max = counter.readline()
    counter.close()
    proxy = urllib2.ProxyHandler({'http': '192.99.43.195:3128'})
    rutr = cookielib.CookieJar()
    opener = build_opener(HTTPCookieProcessor(rutr), proxy)
    response = opener.open(login_url, urlencode(dict_encode(credentials)).encode())
    search = opener.open(search_url)
    soup = BeautifulSoup.BeautifulSoup(search)
    topics = soup.findAll( 'tr', {'class': 'tCenter hl-tr'})
    result = {}
    for x in topics:
        xs = str(x)
        name_id = re.search('viewtopic.+?\/(.+?)[\/\(]', xs)
        if name_id == None:
            continue
        cat_id = re.findall('tracker.php\?f\=(\d+)', xs)[0]
        topic_id = re.findall('viewtopic.php\?t=(\d+)', xs)[0]
        name_id = re.findall('viewtopic.+?\/ (\w.+?) [\/\(]', xs)[0]
        year_id = re.findall('\[(\d{4})', xs)[0]
        result[name_id] = str(year_id)
    return result


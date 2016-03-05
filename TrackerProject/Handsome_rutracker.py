# This Python file uses the following encoding: utf-8

import BeautifulSoup
import urllib2
import re
import cookielib
from urllib import urlencode, quote, unquote
from urllib2 import build_opener, HTTPCookieProcessor
import sqlite3


credentials = {'login_username': u'cheshiremajor', 'login_password': u'ZNt,zK.,k.', 'login': u'Вход',}
login_url = 'http://login.rutracker.org/forum/login.php'
start_url = 'http://rutracker.org/forum/tracker.php?f=2198,2199,2201,2339,312,313'


def dict_encode(dict, encoding='cp1251'):
    """Encode dict values to encoding (default: cp1251)."""
    encoded_dict = {}
    for key in dict:
        encoded_dict[key] = dict[key].encode(encoding)
    return encoded_dict

def parse_rutracker():
    conn = sqlite3.connect('Untitled.sqlite')
    cur = conn.cursor()
    cur.execute(" SELECT LastTime FROM Trackers WHERE ID = 1;")
    last_time = cur.fetchone()[0]
    print last_time
    max_time, torrent_time = last_time, last_time + 1
    x = True
    gap = 50
    int_result = []
    rutr = cookielib.CookieJar()
    opener = build_opener(HTTPCookieProcessor(rutr))
    opener.open(login_url, urlencode(dict_encode(credentials)).encode())
    search_url = start_url
    while x == True:
        search = opener.open(search_url)
        soup = BeautifulSoup.BeautifulSoup(search, fromEncoding="windows-1251")
        topics = soup.findAll('tr', {'class': 'tCenter hl-tr'})
        next =  soup.findAll('a', {'class': 'pg'})
        next_search = re.search(r'search_id\=(\w+)', str(next))
        if next_search:
            search_ID = next_search.group(1)
        search_url = 'http://rutracker.org/forum/tracker.php?search_id=%s&start=%s' % (search_ID, gap)
        gap += 50
        for y in topics:
            xy = str(y)
            temp_torrent = {}
            torrent_time_class = y.findAll('td', {'class': 'row4 small nowrap'})
            torrent_time = re.search('''<u>(\d{10,10})''', str(torrent_time_class))
            torrent_ID = re.search('''viewtopic.php\?t\=(\d{7,7})''', xy)
            movie_name = re.search('''\d{7,7}\"\>(.+?)\(''', xy)
            year = re.search('\[(\d{4})', xy)
            if torrent_ID:
                torrent_ID = int(torrent_ID.group(1))
            if torrent_time:
                torrent_time = int(torrent_time.group(1))
                max_time = max(torrent_time, max_time)
            else:
                continue
            if last_time >= torrent_time:
                print torrent_time
                x = False
                break
            if movie_name and year:
                temp_torrent[u'torrent_ID'] = torrent_ID
                temp_torrent[u'Movie'] = movie_name.group(1).decode('utf-8')
                temp_torrent[u'Year'] = year.group(1)
            else:
                continue
            int_result.append(temp_torrent)
    cur.execute("UPDATE Trackers SET LastTime= ? WHERE Id = 1;", (max_time, ))
    #conn.commit()
    return int_result

test = parse_rutracker()
print len(test), test
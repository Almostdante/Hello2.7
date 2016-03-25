          # This Python file uses the following encoding: utf-8

import BeautifulSoup
import re
import cookielib
from urllib import urlencode, quote, unquote
from urllib2 import build_opener, HTTPCookieProcessor
import sqlite3

search_url = 'http://nnmclub.to/forum/tracker.php?f=954,885,912,227,661'
login_url = 'http://nnmclub.to/forum/login.php'
credentials = {'username': u'almostdante', 'password': u'Welcome2012', 'login': u'Вход',}
next_page_url = 'http://nnmclub.to/forum/tracker.php?search_id=%s&start=%s'


def dict_encode(dict, encoding='cp1251'):
    """Encode dict values to encoding (default: cp1251)."""
    encoded_dict = {}
    for key in dict:
        encoded_dict[key] = dict[key].encode(encoding)
    return encoded_dict


def parse_nnm():
    conn = sqlite3.connect('Untitled.sqlite')
    cur = conn.cursor()
    cur.execute(" SELECT LastTime FROM Trackers WHERE ID = 2;")
    last_time = cur.fetchone()[0]
    print last_time
    max_time, torrent_time = last_time, last_time + 1
    gap = 50
    int_result = []
    headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.151 Safari/535.19' }
    cook = cookielib.CookieJar()
    opener = build_opener(HTTPCookieProcessor(cook))
    opener.open(login_url, urlencode(dict_encode(credentials)).encode())
    url = search_url
    x = True
    while x == True:
        search = opener.open(url)
        soup = BeautifulSoup.BeautifulSoup(search, fromEncoding="windows-1251")
        topics = soup.findAll('tr', {'class': ['prow1', 'prow2']})
        next =  soup.findAll('span', {'class': 'nav'})
        next_search = re.search(r'search_id\=(\w+)', str(next))
        if next_search:
            search_ID = next_search.group(1)
        url = next_page_url % (search_ID, gap)
        gap += 50
        if gap > 450:
            break
        for y in topics:
            xy = str(y)
            temp_torrent = {}
            torrent_time_class = y.findAll('td', {'title': u'Добавлено'})
            torrent_time = re.search('''<u>(\d{10,10})''', str(torrent_time_class))
            torrent_size_class = y.findAll('td', {'title': ''})
            torrent_size = re.search('''<\/u>([0-9, ]+) GB''', xy)
            torrent_ID = re.search('''viewtopic.php\?t\=(\d{6,7})''', xy)
            movie_name = re.search('''viewtopic.php\?t\=\d{6,7}\"\>(.+?)\(''', xy)
            year = re.search('\((\d{4})\)', xy)
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
            if movie_name and year and torrent_size:
                temp_torrent[u'torrent_link'] = 'http://nnmclub.me/forum/viewtopic.php?t=%s' % (torrent_ID,)
                temp_torrent[u'Movie'] = movie_name.group(1).decode('utf-8')
                temp_torrent[u'Year'] = year.group(1)
                if torrent_size:
                    torrent_size = torrent_size.group(1)
                else:
                    torrent_size = '-'
                temp_torrent[u'Size'] = torrent_size
            else:
                continue
            int_result.append(temp_torrent)


    cur.execute("UPDATE Trackers SET LastTime= ? WHERE Id = 2;", (max_time, ))
    #conn.commit()
    return int_result


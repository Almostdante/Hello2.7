# This Python file uses the following encoding: utf-8

import BeautifulSoup
import re
import cookielib
from urllib import urlencode
from urllib2 import build_opener, HTTPCookieProcessor
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "Untitled.sqlite")



def dict_encode(dict, encoding='cp1251'):
    """Encode dict values to encoding (default: cp1251)."""
    encoded_dict = {}
    for key in dict:
        encoded_dict[key] = dict[key].encode(encoding)
    return encoded_dict

def select_untitled(fields, tables, condition):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(" SELECT %s FROM %s WHERE %s;"%(fields, tables, condition))
    result = cur.fetchone()[0]
    conn.close()
    return result

def update_untitled(fields, tables, condition):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    print "UPDATE %s SET %s WHERE %s;"%(tables, fields, condition)
    cur.execute("UPDATE %s SET %s WHERE %s;"%(tables, fields, condition))
    conn.commit()
    conn.close()
    return

def insert_untitled(tables, columns, values):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    print "INSERT OR IGNORE INTO %s (%s) VALUES %s;"%(tables, columns, values)
    cur.execute("INSERT OR IGNORE INTO %s (%s) VALUES %s;"%(tables, columns, values))
    conn.commit()
    conn.close()
    return



class Tracker:

    def __init__(self, db_id, domain):
        self.ID = db_id
        self.domain = domain
        self.gap = 0
        self.page_size = 50
        self.current_last_time = 0
        self.previous_last_time = select_untitled("LastTime", "Trackers", "ID=%s"%(self.ID, ))

    def readtime(self):
        print "Previous_time %s" % (self.previous_last_time)
        return self.previous_last_time

    def writetime(self):
        update_untitled("LastTime", "Trackers", "Id=%s"%(self.id))
        return

    def get_torrents(self):
        int_result = []
        cj = cookielib.CookieJar()
        opener = build_opener(HTTPCookieProcessor(cj))
        opener.open(self.login_url, urlencode(dict_encode(self.credentials)).encode())
        current_url = self.start_url
        x = True
        while x == True:
            current_page = opener.open(current_url)
            soup = BeautifulSoup.BeautifulSoup(current_page, fromEncoding="windows-1251")
            topics = soup.findAll(*self.how_to_find_topics)
            for topic in topics:
                try:
                    torrent_time = int(topic.find(*self.how_to_find_time).u.contents[0])
                    if torrent_time < self.previous_last_time:
                        x = False
                        break
                    self.current_last_time = max(torrent_time, self.current_last_time)
                    torrent_size = round(int(topic.find(*self.how_to_find_size).u.contents[0])/2.0**30, 2)
                    torrent_title = topic.find(*self.how_to_find_name_year_id)
                    torrent_movie_year = re.search(self.movie_year_regexp, str(torrent_title)).group(1)
                    torrent_id = str(re.search('\d+', torrent_title['href']).group(0))
                    torrent_link = self.link_to_torrent_url + torrent_id
                    torrent_download_link = self.link_to_download + torrent_id
                    name_for_class = self.domain.strip()[0] + "_"+ torrent_id
                    for title in str(torrent_title.contents[0]).split('(')[0].split('/'):
                        if title.startswith('<'):
                            continue
                        if re.search('[a-zA-Z]+', title):
                            int_result.append({u'torrent_link' : torrent_link, u'object_name' : name_for_class, u'download_link' : torrent_download_link, u'Movie': title.strip().decode('utf-8'), u'Year': torrent_movie_year, u'Size': torrent_size})
                except:
                    print topic
                    continue
            self.gap += self.page_size
            if self.gap > 40:
                break
            next =  soup.findAll(self.how_to_find_next_page)
            next_search = re.search(r'search_id\=(\w+)', str(next))
            if next_search:
                search_ID = next_search.group(1)
                current_url = self.search_url % (search_ID, self.gap)
                print current_url
            else:
                x = False
        return int_result




rutracker = Tracker(1, 'rutracker.org')
rutracker.credentials = {'login_username': u'cheshiremajor', 'login_password': u'ZNt,zK.,k.', 'login': u'Вход',}
rutracker.login_url = 'http://login.%s/forum/login.php' % (rutracker.domain)
rutracker.start_url = 'http://%s/forum/tracker.php?f=2198,2199,2201,2339,313,930' % (rutracker.domain)
rutracker.how_to_find_topics = ('tr', {'class': 'tCenter hl-tr'})
rutracker.how_to_find_time = ('td', {'class': 'row4 small nowrap'})
rutracker.how_to_find_size = ('td', {'class': 'row4 small nowrap tor-size'})
rutracker.link_to_torrent_url = 'http://%s/forum/viewtopic.php?t=' % (rutracker.domain)
rutracker.link_to_download = 'http://dl.%s/forum/dl.php?t=' % (rutracker.domain)
rutracker.how_to_find_name_year_id = ('a', {'class': ('med tLink hl-tags bold', 'med tLink')})
rutracker.search_url = 'http://rutracker.org/forum/tracker.php?search_id=%s&start=%s' #TODO: how to do double substitute
rutracker.how_to_find_next_page = ('a', {'class': 'pg'})
rutracker.movie_year_regexp = '\[(\d{4})'

rutracker.link_to_download

nnmclub = Tracker(2, 'nnmclub.to')
nnmclub.credentials = {'username': u'almostdante', 'password': u'Welcome2012', 'login': u'Вход',}
nnmclub.login_url = 'http://%s/forum/login.php' % (nnmclub.domain)
nnmclub.start_url = 'http://%s/forum/tracker.php?f=954,885,912,227,661' % (nnmclub.domain)
nnmclub.how_to_find_topics = ('tr', {'class': ('prow1', 'prow2')})
nnmclub.how_to_find_time = ('td', {'title': u'Добавлено'})
nnmclub.how_to_find_size = ('td', {'class': 'gensmall'})
nnmclub.link_to_torrent_url = 'http://%s/forum/viewtopic.php?t=' % (nnmclub.domain)
nnmclub.link_to_download = 'http://%s/forum/download.php?id=' % (nnmclub.domain)
nnmclub.how_to_find_name_year_id = ('a', {'class': ('genmed topictitle', 'seedmed topictitle')})
nnmclub.search_url = 'http://nnmclub.to/forum/tracker.php?search_id=%s&start=%s'
nnmclub.how_to_find_next_page = ('span', {'class': 'nav'})
nnmclub.movie_year_regexp = '\((\d{4})\)'



"""
nnmclub.readtime()
rutracker.readtime()
temp = nnmclub.get_torrents()
temp2 = rutracker.get_torrents()
print len(temp)
print len(temp2)
for x in temp:
    print x
for x in temp2:
    print x
print temp + temp2
"""




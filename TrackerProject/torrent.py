# This Python file uses the following encoding: utf-8

import tracker
import BeautifulSoup
import re
import cookielib
from urllib2 import build_opener, HTTPCookieProcessor



class Torrent:
    def __init__(self, size, link, download_link, year, movie, russian_name):
        self.Torrent_size = size
        self.Full_link_to_topic = link
        self.Link_to_torrent_download = download_link
        self.Movie_year = year
        self.Movie_name = movie
        self.Movie_id = 0
        self.Subtitles = '-'
        self.Resolution = '-'
        self.Duration = '-'
        self.Rate = 0
        self.Director = ''
        self.IMDB_Votes = 0
        self.Metascore = 0
        self.Movie_russian_name = russian_name
        self.Watched = 'N'
    def __str__(self):
        return '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, '%(self.Movie_name, self.Director, self.IMDB_Votes, self.Metascore, self.Movie_id, self.Rate, self.Torrent_size, self.Full_link_to_topic, self.Resolution, self.Duration, self.Subtitles)
    def check_in_db(self):
        if self.Movie_id:
            try:
                self.Rate, self.Director, self.IMDB_Votes, self.Metascore, self.Watched = tracker.select_untitled("IMDB_rating, Director, IMDB_Votes, Metascore, Watched", "Movies", "IMDB_ID = %s"%(self.Movie_id, ))[0]
            except:
                return 0
        else:
            try:
                self.Rate, self.Movie_id, self.Director, self.IMDB_Votes, self.Metascore, self.Watched = tracker.select_untitled("IMDB_rating, IMDB_ID, Director, IMDB_Votes, Metascore, Watched", "Movies", "Original_name = '%s'"%(self.Movie_name, ))[0]
            except:
                return 0
        return self.Rate
    def parse_link(self):
        cj = cookielib.CookieJar()
        opener = build_opener(HTTPCookieProcessor(cj))
        page = opener.open(self.Full_link_to_topic)
        if self.Full_link_to_topic.startswith('http://rutr'):
            soup = BeautifulSoup.BeautifulSoup(page, fromEncoding="windows-1251")
        else:
            soup = BeautifulSoup.BeautifulSoup(page)
        title = soup.findAll(['a', 'h1'], {'class': 'maintitle'})
        post = soup.findAll(['div', 'span'], {'class': ['postbody', 'post_body']})
        post = str(post).decode(encoding='utf-8')
        post = unicode(post)
        try:
            self.Movie_id = str(re.search(r'(tt\d{7})', post).group(0))
        except:
            pass
        try:
            self.Resolution = re.search(r'[0-9]{3,4}p', str(title)).group(0)
        except:
            pass
        try:
            self.Duration = re.search(ur'родолжительно\w+?\:*<\/span\>\:* ([0-9:]+)', post, re.UNICODE).group(1)
        except:
            pass
        self.Subtitles = 'Y' if (re.search(ur'титр.{,70}(\w*?(усск|rus|Rus))', post, re.UNICODE) or re.search(ur'(усск|rus|Rus).{,18}(\w*?титр\w*?)', post, re.UNICODE)) else "-"
        return
    def append_torrent_for_mail(self, *m):
        for list in m:
            if self.Rate > 7.0:
                if str(list.keys()[0]) in tracker.mymail and self.Watched == 'Y':
                    continue
                else:
                    list[list.keys()[0]].append([self.Movie_name + ' (' + self.Movie_russian_name.strip() +')', self.Movie_year, self.Director.encode('ascii', 'replace'), self.Rate, self.IMDB_Votes, self.Metascore, self.Subtitles, self.Torrent_size, '<a href=%s>F</a>'%self.Full_link_to_topic, '<a href=%s>D</a>'%self.Link_to_torrent_download])



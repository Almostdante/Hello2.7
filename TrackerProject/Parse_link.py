# This Python file uses the following encoding: utf-8

import re
import BeautifulSoup
import urllib2
link_rutr = 'http://dl.rutracker.org/forum/dl.php?t='
link_nnm = 'http://nnmclub.to/forum/download.php?id='
test = [{u'torrent_link': 'http://nnm-club.me/forum/viewtopic.php?t=993600', u'Year': '2015', u'Movie': u'<b>\u041c\u0430\u043b\u044b\u0448 / Little Boy '}, {u'torrent_link': 'http://rutracker.org/forum/viewtopic.php?t=5182835', u'Movie': u'\u041f\u0438\u043d\u043e\u043a\u043a\u0438\u043e / Pinocchio ', u'Year': '2013'}]


def parse_link(link):
    page = urllib2.urlopen(link).read()
    id = re.search('[0-9]{6,}', link).group(0)
    if link.startswith('http://rutr'):
        soup = BeautifulSoup.BeautifulSoup(page, fromEncoding="windows-1251")
        linktofile = link_rutr + id
    else:
        soup = BeautifulSoup.BeautifulSoup(page)
        linktofile = link_nnm + id
    title = soup.findAll(['a', 'h1'], {'class': 'maintitle'})
    resolution = re.search(r'[0-9]{3,4}p', str(title))
    if resolution:
        resolution = resolution.group(0)
    else:
        resolution = '-'
    post = soup.findAll(['div', 'span'], {'class': ['postbody', 'post_body']})
    post = str(post).decode(encoding='utf-8')
    post = unicode(post)
    duration = re.search(ur'родолжительно\w+?\:*<\/span\>\:* ([0-9:]+)', post, re.UNICODE)
    if duration:
        duration = duration.group(1)
    else:
        duration = '-'
#    subtitles = re.search(ur'убтитр\w+?\:*<\/span\>\:* (\w+?усск\w+?)\<', post, re.UNICODE)
    subtitles = re.search(ur'титр.{,70}(\w*?(усск|rus|Rus))', post, re.UNICODE)
    subtitles1 = re.search(ur'(усск|rus|Rus).{,18}(\w*?титр\w*?)', post, re.UNICODE)

    if subtitles:
        subtitles = 'Y'
    elif subtitles1:
        subtitles = 'Y'
    else:
        subtitles = '-'
    return {'Resolution': resolution, 'Duration': duration ,'Subtitles': subtitles, 'Linktofile': linktofile}


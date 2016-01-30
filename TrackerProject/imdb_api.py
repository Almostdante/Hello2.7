import urllib2
import json
import re

def IMDB_Search(moviename, movieyear):
    url  = 'http://www.imdb.com/xml/find?json=1&nr=1&tt=on&q='+moviename
    urll = urllib2.urlopen(urllib2.Request(url)).read()
    js = json.loads(urll)
    candidates = []
    for x in js.keys():
        for y in js[x]:
            if (y[u'title'] == moviename or y[u'title'] == 'The ' +moviename):
                print y[u'title']
                if y[u'description'].startswith(movieyear):
                    print y
                    candidates.append({'id': y[u'id'], 'title':y[u'title'], 'descr':y[u'description']})
    for x in candidates:
        url = 'http://www.imdb.com/title/' + x['id'] +'/'
        print url
        data = urllib2.urlopen(urllib2.Request(url)).read()
#        data = open(url).read()
#        print data
        rateIMDB = re.findall('([0-9,.]+) IMDb users have given a weighted average vote of ([0-9.]+)', data)
        rateMeta = re.findall('(\d+) review excerpts provided by Metacritic.com" > (\d+)/100', data)
        print rateIMDB, rateMeta
        x['IMDB_Users'] = rateIMDB[0][0]
        x['IMDB_Rating'] = rateIMDB[0][1]
        if len(rateMeta) > 0:
            x['Meta_Critics'] = rateMeta[0][0]
            x['Meta_Rating'] = rateMeta[0][1]
        else:
            x['Meta_Critics'] = '0'
            x['Meta_Rating'] = '0'
#        print data
    return candidates
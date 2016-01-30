          # This Python file uses the following encoding: utf-8

import urllib2
import json
import re
import time
global z
z = 1


def IMDB_Search(moviename, movieyear):
    if moviename.startswith('Dal'):
        return
    moviename_ = re.sub(r"\s+", '+', moviename)
    url = 'http://www.omdbapi.com/?t='+moviename_+'&y='+movieyear+'&plot=full&r=json'
    urll = urllib2.Request(url)
    urlll = urllib2.urlopen(urll)
    urllll = urlll.read()
    js = json.loads(urllll)
    for x in js:
       js[x] = js[x].encode('utf-8')
    result1 = {}
    if js.get('Error', 0) == 0:
        result2 = [str('Title: '+moviename).ljust(50), str('Director: '+js['Director']).ljust(30), str('Rating: '+js['imdbRating']),  str('Votes: '+js['imdbVotes']).ljust(14), str('Metascore: '+js['Metascore'])]
        result1 = {'Title':moviename, 'Director':js['Director'], 'Rating':round(js['imdbRating'], 1), 'Votes':js['imdbVotes'], 'Metascore':js['Metascore']}
    else:
        print moviename, 'Not Found'
        return
    print result1
    return result1

'''
def IMDB_Search_old(moviename, movieyear):
    url  = 'http://www.imdb.com/xml/find?json=1&nr=1&tt=on&q='+moviename
    print url
    urll = urllib2.urlopen(urllib2.Request(url)).read()
    js = json.loads(urll)
    print js
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
'''

#print IMDB_Search('crimson peak', '2015')

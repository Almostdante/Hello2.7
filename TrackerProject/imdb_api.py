          # This Python file uses the following encoding: utf-8

import urllib2
import json
import re
import time
global z
z = 1


def IMDB_Search(moviename, movieyear):
    moviename_ = re.sub(r"\s+", '+', moviename)
    url = u'http://www.omdbapi.com/?t=%s&y=%s&plot=full&r=json' % (moviename_, movieyear)
    urlll = urllib2.urlopen(url.encode("UTF-8")).read()
    js = json.loads(urlll)
    for x in js:
        print x
        result1 = {}
        if js.get('Error', 0) == 0:
            result1 = {'Title':moviename, 'Director':js['Director'], 'Rating':js['imdbRating'], 'Votes':js['imdbVotes'], 'Metascore':js['Metascore'], 'IMDB_ID':js['imdbID']}
        else:
            print moviename, 'Not Found'
            result1 = {'Title':moviename, 'Director':'-', 'Rating':'-', 'Votes':'-', 'Metascore':'-', 'IMDB_ID':'-'}
    print result1
    return result1
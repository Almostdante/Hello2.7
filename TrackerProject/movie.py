import re
import urllib2
import json

class Movie:
    def __init__(self, name, year, movie_id = ''):
        self.IMDB_ID = movie_id
        self.Original_name = name
        self.Russian_name = ''
        self.Director = ''
        self.Year = year
        self.IMDB_Rating = 0
        self.IMDB_Votes = 0
        self.Metascore = 0
        self.Watched = ''
    def __str__(self):
        return '%s, %s, %s, %s, %s, %s, %s, '%(self.Original_name, self.Director, self.Year, self.IMDB_ID, self.IMDB_Rating, self.IMDB_Votes, self.Metascore)
    def check_imdb(self):
        if self.IMDB_ID == '':
            url = u'http://www.omdbapi.com/?t=%s&y=%s&plot=full&r=json' % (re.sub(r"\s+", '+', self.Original_name), self.Year)
        elif len(self.IMDB_ID) == 9:
            url = u'http://www.omdbapi.com/?i=%s&plot=short&r=json'%(self.IMDB_ID)
        else:
            print 'WTF in ID??' + self.IMDB_ID
        try:
            urlll = urllib2.urlopen(url.encode("UTF-8")).read()
            js = json.loads(urlll)
        except:
            print "Error in OMDB API"
            return 0
        try:
            if js[u'Response'] == u'False':
                return 0
        except:
            pass
        try:
            self.Director = str(js['Director']).encode('ascii', 'replace')
        except:
            print js
        try:
            self.IMDB_Rating = float(js['imdbRating'].replace(',', '.'))
        except:
            try:
                self.IMDB_Rating = float(js['imdbRating'])
            except:
                self.IMDB_Rating = 0
        try:
            self.IMDB_Votes = int(js['imdbVotes'].split(',')[0])
        except:
            self.IMDB_Votes = 0
        try:
            self.Metascore = int(js['Metascore'])
        except:
            pass
        self.IMDB_ID = str(js['imdbID'])
#        print self.Original_name + "Movie not found"
        return self.IMDB_Rating

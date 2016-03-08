import urllib2
import BeautifulSoup
import sqlite3
import re

url = 'http://www.imdb.com/user/ur15497815/ratings?start=1&view=compact&sort=ratings_date:desc'


def Watchlist_Update():
    conn = sqlite3.connect('Untitled.sqlite')
    cur = conn.cursor()
    cur.execute(" SELECT LastTime FROM Trackers WHERE ID = 3;")
    count_of_watched = cur.fetchone()[0]

    page = urllib2.urlopen(url)
    soup = BeautifulSoup.BeautifulSoup(page)
    list_of_films = soup.findAll('td', {'class': 'title'})


    if len(list_of_films) - count_of_watched > 0:
        for x in list_of_films[0:(len(list_of_films) - count_of_watched)]:
            cur.execute("UPDATE Movies SET watched = 'Y' WHERE IMDB_ID = ?;", (re.search('title\/(tt[0-9]*)', str(x)).group(1), ))
        cur.execute("UPDATE Trackers SET Lasttime = ? WHERE ID = 3;", (len(list_of_films), ))
    conn.commit()
    return


#print list_of_films
#print len(list_of_films)

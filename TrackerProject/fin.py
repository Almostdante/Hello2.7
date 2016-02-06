          # This Python file uses the following encoding: utf-8


from Beautiful_NNM import parse_nnm
from Handsome_rutracker import parse_rutr
from imdb_api import IMDB_Search
import smtplib
from texttable import Texttable
fromaddr = 'almostdante@gmail.com'
toaddrs  = 'admitrie@icloud.com'

username = 'almostdante'
password = 'haeytscqnadbomtv'

#nnm = parse_nnm()
#rutr = parse_rutr()
#all = dict(nnm.items() + rutr.items())
all = {'Spartacus': '1960', 'Queen of the Desert': '2015', "Je t'aime je t'aime": '1968', 'Woodlawn': '2015', 'Wong Fei Hung: Chi tit gai dau neung gung': '1993', 'Stealth': '2005', 'Martyrs': '2015', 'Crimson Peak': '2015', 'God of Gamblers 3: Back to Shanghai': '1991', 'Captain Lightfoot': '1955', 'Ant-Man': '2015', 'Variet&#233;': '1925', 'The Raid 2: Berandal': '2014', 'The 33': '2015', 'Marmaduke': '2010', 'Shenandoah': '1965', 'The Devil&rsquo;s Violinist': '2013', 'The Walk': '2015', 'Flubber': '1997', 'Wandafuru raifu': '1998', 'Midnight Express': '1978', 'Skyfall': '2012', 'Need for Speed': '2014', 'Criminal Activities': '2015', 'Hotel Transylvania 2': '2015', 'Harbinger Down': '2015', 'Legend': '2015', 'Knock Knock': '2014', 'The Hunger Games: Catching Fire': '2013', 'Schone Handen': '2015', 'Terminus': '2015', 'The Last Witch Hunter': '2015', 'The Postman Always Rings Twice': '1981', 'Heist': '2015', 'La Belle Saison': '2015', 'Sharktopus vs. Whalewolf': '2015', 'Spectre': '2015', 'Love the Coopers': '2015', 'Peggy Sue Got Married': '1986', 'Streets of Fire': '1984', 'Forbidden Planet': '1956', 'Marie-Antoinette reine de France': '1956', 'The Mortal Instruments: City of Bones': '2013', 'Taxi': '2015', 'Tokyo!': '2008', 'Jeruzalem': '2015', 'The Master': '1992', 'Death Proof': '2007', 'Synchronicity': '2015', 'Macbeth': '2015', 'All That Heaven Allows': '1955', "National Lampoon's Vegas Vacation": '1997', 'Scouts Guide to the Zombie Apocalypse': '2015', 'The Program': '2015', 'Dallas Buyers Club': '2013', 'Maleficent': '2014', 'The Purge: Anarchy': '2014', 'Earth to Echo': '2014', 'Painkillers': '2015'}
all = {'Peggy Sue Got Married': '1986', 'Streets of Fire': '1984', 'Forbidden Planet': '1956', 'Marie-Antoinette reine de France': '1956', 'The Mortal Instruments: City of Bones': '2013', 'Taxi': '2015', 'Tokyo!': '2008', 'Jeruzalem': '2015', 'The Master': '1992', 'Death Proof': '2007', 'Synchronicity': '2015', 'Macbeth': '2015', 'All That Heaven Allows': '1955', "National Lampoon's Vegas Vacation": '1997', 'Scouts Guide to the Zombie Apocalypse': '2015', 'The Program': '2015', 'Dallas Buyers Club': '2013', 'Maleficent': '2014', 'The Purge: Anarchy': '2014', 'Earth to Echo': '2014', 'Painkillers': '2015'}
print all
print len(all)
listt = []

for x, y in all.items():
    listt.append(IMDB_Search(x, y))

# listt = [{('Title': 'moviename'), 'Director':"s[u'Director']", 'Votes': "js[u'imdbVotes']", 'Rating':"js[u'imdbRating']", 'Metascore': 123}, {'Title': 'moviename', 'Director':"s[u'Director']", 'Votes': "js[u'imdbVotes']", 'Rating':"js[u'imdbRating']", 'Metascore': 123}, {'Title': 'moviename', 'Director':"s[u'Director']", 'Votes': "js[u'imdbVotes']", 'Rating':"js[u'imdbRating']", 'Metascore': 123},{'Title': 'moviename', 'Director':"s[u'Director']", 'Votes': "js[u'imdbVotes']", 'Rating':"js[u'imdbRating']", 'Metascore': 123}]

t = Texttable()
t.add_row(['Title', 'Director', 'Rating', 'Votes', 'MS'])
t.set_cols_width ([20,15,6,6,3])
for x in listt:
    try:
        t.add_row([x['Title'], x['Director'], x['Rating'],  x['Votes'], x['Metascore']])
    except:
        pass
#text = ''
#print listt
#print len(listt)
#for i in listt:
#    text = text + str(i) +'\n'
print t.draw()


msg = t.draw()
# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
    # This Python file uses the following encoding: UTF-8
from Beautiful_NNM import parse_nnm
from Handsome_rutracker import parse_rutracker
from Parse_link import parse_link
from imdb_api import IMDB_Search
from Watchlist_IMDB_Parse import Watchlist_Update
import sqlite3
from itertools import groupby
from operator import itemgetter
import unicodedata
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os.path

fromaddr = 'almostdante@gmail.com'
toaddr  = 'almostdante@gmail.com'
toaddr2 = 'vtonad@mail.ru'
username = 'almostdante'
password = 'haeytscqnadbomtv'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "Untitled.sqlite")

conn = sqlite3.connect('Untitled.sqlite')
cur = conn.cursor()

cur.execute("SELECT max(ID) FROM Torrents ;")
maxID = cur.fetchone()[0]
print maxID

all = parse_nnm() + parse_rutracker()
print len(all), all


for x in all[:]:
    if len(x[u'Movie'].split('/')) <= 1:
        continue
    x_name = x[u'Movie'].split('/')[-1].strip()
    x_ru_name = x[u'Movie'].split('/')[0].strip()
    cur.execute("SELECT IMDB_rating FROM Movies WHERE Original_name = ?;", (x_name, ))
    rating = cur.fetchone()
    if not rating:
        rate = (IMDB_Search(x_name, unicode(x[u'Year'])))
        rating = float(rate['Rating'])
        try:
            rate['Votes'] = round(float(rate['Votes'])/1000, 2)
        except:
            rate['Votes'] = rate['Votes'].split(',')[0]
        cur.execute("SELECT * FROM Movies WHERE IMDB_ID = ?;", (rate['IMDB_ID'], ))
        if not cur.fetchone():
            cur.execute('''INSERT OR IGNORE INTO Movies (IMDB_ID, Original_name, Russian_name, Director, Year, IMDB_Rating, IMDB_Votes, Metascore)
            VALUES ( ?, ?, ?, ?, ?, ?, ?, ? )''', ( rate['IMDB_ID'], x_name, x_ru_name, rate['Director'], x[u'Year'], rate['Rating'], rate['Votes'], rate['Metascore'] ) )
        if rating < 7.2:
            continue
    else:
        rating = rating[0]
    if rating < 7.2 or rating == 'N/A':
        continue

    #print 'And we have a winner  __' + x[u'Movie'] + '____' + str(rating)
    temp = parse_link(x[u'torrent_link'])
    cur.execute("SELECT IMDB_ID FROM Movies WHERE Original_name = ?;", (x_name, ))
    movieID = cur.fetchone()[0]
    cur.execute('''INSERT OR IGNORE INTO Torrents (MovieID, Link, Torrent_File, File_Size, Subtitles, Resolution, Duration)
    VALUES ( ?, ?, ?, ?, ?, ?, ? )''', ( movieID, x[u'torrent_link'], temp['Linktofile'], x[u'Size'], temp['Subtitles'], temp['Resolution'], temp['Duration']  ) )
    conn.commit()

Watchlist_Update()

cur.execute("SELECT Original_name, Russian_name, Year, Director, IMDB_Rating, IMDB_Votes, Metascore, Subtitles, Resolution, File_size, Link, Torrent_File, Watched FROM Torrents JOIN Movies ON Movies.IMDB_ID = Torrents.MovieID WHERE Torrents.ID > ?;", (maxID, ))
today_list = cur.fetchall()
maillist = []
maillist_N = []


today_list.sort()
for x in today_list:
    x = (unicodedata.normalize('NFKD', (x[0]+ ' ('+ x[1].strip() + ')')).encode('utf-8','ignore'), x[2], unicodedata.normalize('NFKD', x[3]).encode('utf-8','ignore').split(',')[0], x[4], x[5], x[6], unicodedata.normalize('NFKD', x[7]).encode('utf-8','ignore'), x[9], '<a href=%s>F</a>'% x[10], '<a href=%s>D</a>'% x[11])
    maillist_N.append(x)
    print x
    if x[12] != 'Y':
        maillist.append(x)


FULL_HTML = []
today_list.sort()
for name, rows in groupby(maillist, itemgetter(0)):
     table = []
     for Name, Year, Director, IMDB_Rating, IMDB_Votes, Metascore, Subtitles, File_Size, Tracker_Link, Torrent_File in rows:
        table.append(
            "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td></tr>".format(
                Name, Year, Director, IMDB_Rating, IMDB_Votes, Metascore, Subtitles, File_Size, Tracker_Link, Torrent_File))

     table = '<table class="fixed"><col width="420px" />\n<col width="50px" />\n<col width="200px" />\n<col width="50px" />\n<col width="50px" />\n<col width="50px" />\n<col width="30px" />\n<col width="50px" />\n<col width="20px" />\n<col width="20px" />\n{}\n</table>'.format('\n'.join(table))
     FULL_HTML.append(table)

FULL_HTML = "<html>\n{}\n</html>".format('\n'.join(FULL_HTML))

# print FULL_HTML

FULL_HTML2 = []
today_list.sort()
for name, rows in groupby(maillist_N, itemgetter(0)):
     table = []
     for Name, Year, Director, IMDB_Rating, IMDB_Votes, Metascore, Subtitles, File_Size, Tracker_Link, Torrent_File in rows:
        table.append(
            "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td></tr>".format(
                Name, Year, Director, IMDB_Rating, IMDB_Votes, Metascore, Subtitles, File_Size, Tracker_Link, Torrent_File))

     table = '<table class="fixed"><col width="420px" />\n<col width="50px" />\n<col width="200px" />\n<col width="50px" />\n<col width="50px" />\n<col width="50px" />\n<col width="30px" />\n<col width="50px" />\n<col width="20px" />\n<col width="20px" />\n{}\n</table>'.format('\n'.join(table))
     FULL_HTML2.append(table)

FULL_HTML2 = "<html>\n{}\n</html>".format('\n'.join(FULL_HTML2))




# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Torrents Daily"
msg['From'] = fromaddr
msg['To'] = toaddr
msg2 = MIMEMultipart('alternative')
msg2['Subject'] = "Torrents Daily"
msg2['From'] = fromaddr
msg2['To'] = toaddr2

# Create the body of the message (a plain-text and an HTML version).
text = "blank"
html = FULL_HTML
html2 = FULL_HTML


# Record the MIME types of both parts - text/plain and text/html.
part1_text = MIMEText(text, 'plain')
part1_html = MIMEText(html, 'html')
part2_html = MIMEText(html2, 'html')


# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1_text)
msg.attach(part1_html)
msg2.attach(part1_text)
msg2.attach(part2_html)
# Send the message via local SMTP server.
mail = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo()

mail.starttls()

mail.login(username, password)
mail.sendmail(fromaddr, toaddr, msg.as_string())
mail.sendmail(fromaddr, toaddr2, msg2.as_string())
mail.quit()


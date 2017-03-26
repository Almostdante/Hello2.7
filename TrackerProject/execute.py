# This Python file uses the following encoding: utf-8


import tracker
import torrent
import movie
import smtplib
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from itertools import groupby
from operator import itemgetter

fromaddr = 'almostdante@gmail.com'
Me  = 'almostdante@gmail.com'
She = 'vtonad@mail.ru'
username = 'almostdante'
password = 'haeytscqnadbomtv'
maillist_A = {Me: []}
maillist_N = {She: []}



today_list_rutracker = tracker.rutracker.get_torrents()
today_list_nnm = tracker.nnmclub.get_torrents()
#today_list_nnm = []
#today_list_rutracker = []
today_list = today_list_rutracker + today_list_nnm

print "Today we have %s torrents from NNM and %s torrents from Rutracker"% (len(today_list_nnm), len(today_list_rutracker))
list_of_torrents = []
list_of_movies = []
for x in today_list:
    list_of_torrents.append(torrent.Torrent(x[u'Size'], x[u'torrent_link'], x[u'download_link'],  x[u'Year'], x[u'Movie'].encode('ascii','ignore'), x[u'Russian_name']))



for y in list_of_torrents:
    if not y.check_in_db():
        y.parse_link()
        if y.Movie_id:
            y.check_in_db()
            list_of_movies.append(movie.Movie(y.Movie_name, y.Movie_year, y.Movie_id, y.Movie_russian_name))
        else:
            list_of_movies.append(movie.Movie(y.Movie_name, y.Movie_year, Russian_name = y.Movie_russian_name))
        if list_of_movies[-1].check_imdb():
            y.Movie_id, y.Rate, y.Director, y.IMDB_Votes, y.Metascore = list_of_movies[-1].IMDB_ID, list_of_movies[-1].IMDB_Rating, list_of_movies[-1].Director, list_of_movies[-1].IMDB_Votes, list_of_movies[-1].Metascore
            y.check_in_db()
    elif y.Rate > 6.9:
        y.parse_link()
    y.append_torrent_for_mail(maillist_A, maillist_N)

for q in list_of_movies:
    if q.IMDB_Rating:
        tracker.insert_untitled("Movies", "IMDB_ID, Original_name, Russian_name, Director, Year, IMDB_Rating, IMDB_Votes, Metascore, Updated", (q.IMDB_ID, q.Original_name, q.Russian_name, q.Director, q.Year, q.IMDB_Rating, q.IMDB_Votes, q.Metascore, str(datetime.datetime.now().date())))

#for m in (maillist_A, maillist_N):
maillist_A = {Me: sorted (maillist_A.values()[0], key=lambda t: (t[1], t[0]), reverse = True)}

for m in (maillist_A, ):

    FULL_HTML = []
    today_list.sort()
    for name, rows in groupby(m.values()[0], itemgetter(0)):
        table = []
        for Name, Year, Director, IMDB_Rating, Metascore, Subtitles, Tracker_Link in rows:
            table.append(
                "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td></tr>".format(
                    Name, Year, Director, IMDB_Rating, Metascore, Subtitles, Tracker_Link))

        table = '<table class="fixed"><col width="540px" />\n<col width="50px" />\n<col width="180px" />\n<col width="70px" />\n<col width="30px" />\n<col width="50px" />\n<col width="60px" />\n{}\n</table>'.format('\n'.join(table))
        FULL_HTML.append(table)
    FULL_HTML = "<html>\n{}\n</html>".format('\n'.join(FULL_HTML))


    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Torrents Daily"
    msg['From'] = fromaddr
    msg['To'] = m.keys()[0]


    # Create the body of the message (a plain-text and an HTML version).
    text = "blank"
    html = FULL_HTML


    # Record the MIME types of both parts - text/plain and text/html.
    part1_text = MIMEText(text, 'plain')
    part1_html = MIMEText(html, 'html')


    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1_text)
    msg.attach(part1_html)
    # Send the message via local SMTP server.
    mail = smtplib.SMTP('smtp.gmail.com', 587)

    mail.ehlo()

    mail.starttls()

    mail.login(username, password)
    mail.sendmail(fromaddr, m.keys()[0], msg.as_string())
    mail.quit()

tracker.nnmclub.writetime()
tracker.rutracker.writetime()
tracker.Watchlist_Update()

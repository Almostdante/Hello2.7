import tracker
import torrent
import movie
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromaddr = 'almostdante@gmail.com'
toaddr  = 'almostdante@gmail.com'
toaddr2 = 'vtonad@mail.ru'
username = 'almostdante'
password = 'haeytscqnadbomtv'


today_list_rutracker = tracker.rutracker.get_torrents()
#today_list_nnm = tracker.nnmclub.get_torrents()
today_list_nnm = []
today_list = today_list_rutracker

print "Today we have %s torrents from NNM and %s torrents from Rutracker"% (len(today_list_nnm), len(today_list_rutracker))

list_of_torrents = []
list_of_movies = []
for x in today_list:
    list_of_torrents.append(torrent.Torrent(x[u'Size'], x[u'torrent_link'], x[u'download_link'],  x[u'Year'], x[u'Movie'].encode('ascii','ignore')))

for y in list_of_torrents:
    temp_rate = y.check_rating_in_db()
    if temp_rate > 0.1 and temp_rate < 6.9:
        continue
    elif temp_rate > 7.0:
        y.parse_link()
        continue
    else:
        y.parse_link()
        if y.Movie_id:
            list_of_movies.append(movie.Movie(y.Movie_name, y.Movie_year, y.Movie_id))
        else:
            list_of_movies.append(movie.Movie(y.Movie_name, y.Movie_year))
        list_of_movies[-1].check_imdb()
        y.Movie_id, y.Rate, y.Director, y.IMDB_Votes, y.Metascore  = list_of_movies[-1].IMDB_ID, list_of_movies[-1].IMDB_Rating, list_of_movies[-1].Director, list_of_movies[-1].IMDB_Votes, list_of_movies[-1].Metascore

for q in list_of_movies:
    tracker.insert_untitled("Movies", "IMDB_ID, Original_name, Russian_name, Director, Year, IMDB_Rating, IMDB_Votes, Metascore", (q.IMDB_ID, q.Original_name, q.Russian_name, q.Director, q.Year, q.IMDB_Rating, q.IMDB_Votes, q.Metascore))

maillist = []
for z in list_of_torrents:
    if z.Rate > 6.9:
        maillist.append([z.Movie_name, z.Movie_year, z.Director, z.Rate, z.IMDB_Votes, z.Metascore, z.Subtitles, z.Torrent_size, '<a href=%s>F</a>'%z.Full_link_to_topic, '<a href=%s>D</a>'%z.Link_to_torrent_download])


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

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Torrents Daily"
msg['From'] = fromaddr
msg['To'] = toaddr


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
mail.sendmail(fromaddr, toaddr, msg.as_string())
mail.quit()





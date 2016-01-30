          # This Python file uses the following encoding: windows-1251

import re
import urllib2
url = 'http://nnm-club.me/forum/tracker.php'
def parse_nnm(url):
    final = {}
    count = 0

    headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.151 Safari/535.19' }
    req = urllib2.Request(url, '', headers)
    urll = urllib2.urlopen(req).readlines()
    for line in urll:
        m = re.findall('<a.+genmed topic.+\/(.+?\([0-9]+\))', line)
        if m:
            n = m[0].split('(')
            final[n[0].strip()] = n[1][:-1]
            count += 1
    print len(final)
    return final

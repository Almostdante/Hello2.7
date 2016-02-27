import json
import urllib

summ = 0
countt = 0
jsonn = json.loads(urllib.urlopen('http://python-data.dr-chuck.net/comments_42.json').read())['comments']
#test = sum(jsonn[0]['count'])
#print test
for c in jsonn:
   summ = summ + int(c['count'])
   countt = countt + 1
print 'Count:', countt
print 'Sum:', summ

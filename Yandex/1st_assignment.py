__author__ = 'andreydmitriev'
import re
import pandas


data = pandas.read_csv('titanic.csv', index_col='PassengerId')

print data.groupby(u'Sex').size()

print data.groupby(u'Survived').size().apply(lambda x: float(x) / data.groupby(u'Survived').size().sum()*100)

print data.groupby(u'Pclass').size().apply(lambda x: float(x) / data.groupby(u'Survived').size().sum()*100)

print data[u'Age'].mean()

print data.corr(method='pearson')

print data.axes

listfemalesname = list(data[data.Sex == 'female'][u'Name'])

print listfemalesname

firstname = []
for x in listfemalesname:
    if re.match('.*\(\w*', x):
        firstname.append(re.match('.*\(\w*', x).group().split('(')[1])
    else:
        firstname.append(x.split()[2])
print firstname

d = {}
for i in firstname:
    d[i] = d.get(i, 0) + 1
result = max(d.iteritems(), key=lambda x: x[1])
print result
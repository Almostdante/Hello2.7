          # This Python file uses the following encoding: windows-1251

str2 = 'fsордоdf'
str1 = u'Jean-Marc Vall\xe9e'
str1 = str1.encode('utf-8')

print type(str1)
str3 = str1 + str2
print str3
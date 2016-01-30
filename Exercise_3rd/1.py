S =  raw_input('Enter string')
x = 0
y = []
for char in S:
    print ord(char)
    x += ord(char)
    y.append(ord(char))
print 'sum:', x
print y
print list(map(ord, S))  #Запомнить!!!!
import shelve
db = shelve.open('pers_db')

print len(db)
print db.keys()

sue = db['Sue Jones']

print sue.lastName()
for x in db:
    print x, db[x]
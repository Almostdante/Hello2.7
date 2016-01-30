import person
import shelve

bob = person.Person('Bob Smith')
sue = person.Person('Sue Jones', job='dev', pay=100000)
tom = person.Manager('Tom Jones', 50000)

import shelve
db = shelve.open('pers_db')
for object in (bob, sue, tom):
    db[object.name] = object
db.close()

print person.Person.__
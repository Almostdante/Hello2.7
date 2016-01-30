from person import Person

bob = Person('John')
print bob, '\n', bob.__class__
for key in bob.__dict__.keys():
    print key, ' : ', getattr(bob, key)
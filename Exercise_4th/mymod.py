def CL(file):
    return len(file.readlines())
def CC(file):
    return len(file.read())
def test(name):
    t = open(name)
    ccf = CC(t)
    t.seek(0)
    clf = CL(t)

    print 'This file contains ' + str(clf) +' strings and ' + str(ccf) + ' chars'
    return clf, ccf

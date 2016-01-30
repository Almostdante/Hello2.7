class AttrDisplay:
    def gatherAttrs(self):
        attrs = []
        methods = []
        for key in sorted(dir(self)):
            if key.startswith('__') or (str(getattr(self, key)).find('method') + 1):
                methods.append('%s=%s' % (key, getattr(self, key)))
            else:
                attrs.append('%s=%s' % (key, getattr(self, key)))
        return ', '.join(attrs)

    def __str__(self):
        return '[%s: %s]' % (self.__class__.__name__, self.gatherAttrs())

if __name__ == '__main__':
    class TopTest(AttrDisplay):
        count = 0

        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count+1
            TopTest.count += 2


    class SubTest(TopTest):
        pass
    X, Y = TopTest(), SubTest()
    print(X)
    print(Y)

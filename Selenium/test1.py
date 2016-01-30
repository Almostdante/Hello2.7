#encoding: Windows-1251

class FirstClass:
    def setdata(self, value):
        self.data = value
    def display(self):
        print(self.data)

class SecondClass(FirstClass):
    def display(self):
        print 'Current value = ', [x for x in self.data]

class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value
    def __add__(self, other):
        return ThirdClass(self.data + other)
    def __str__(self):
        return 'ThirdClass: '+ str(self.data)
    def mul(self, other):
        self.data = self.data *other
        return  self.data

Fx = FirstClass()
Fx.setdata('test')
Sx = SecondClass()
Sx.data = ['second', Fx.data]
Fx.data = 'test2'
datax = Fx.data
Fx.name = 'name'
datax = Fx.name
Tx = ThirdClass('ssdfsd')
print dir(Tx)
Tx.display()
print Tx
Ty = Tx + 'afdfdsf'
Ty.display()
print Tx, Ty
ThirdClass.data = 'test'
print Tx.data, Ty.data, ThirdClass.data
print Tx.__dict__.keys(), Fx.__dict__.keys(), SecondClass.__dict__.keys(), ThirdClass.__module__
print '-'*80
def upperData(self):
    return self.data.upper()
print upperData(Tx), upperData(Fx)

ThirdClass.upper = upperData

print Tx.upper()
print ThirdClass.upper(Tx)
#Fx.display()
#Sx.display()
#print datax
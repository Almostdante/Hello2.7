# coding: Windows-1251
from abc import abstractmethod, ABCMeta
from ClassDisplay import AttrDisplay


class Person(AttrDisplay):

    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent/100.00))


class Manager(Person):

#    __metaclass__ = ABCMeta
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

#    @abstractmethod
    def giveRaise(self, percent, bonus=10):
        Person.giveRaise(self, percent + bonus)
#       self.pay = int(self.pay * (1 + percent+bonus/100.00))

if __name__ == '__main__':
    bob = Person('Bob Smith')                        # Тестирование класса
    sue = Person('Sue Jones', job='dev', pay=100000)  # Запустит __init__  автоматически
    print bob.lastName(), bob.pay                          # Извлечет атрибуты
    sue.giveRaise(15)
    print sue.name, sue.pay
    print sue
    tom = Manager('Tom Jones', 150000)
    tom.giveRaise(10)
    print(tom.lastName())
    print(tom)
    print(tom.__class__)

# m = Manager('qwe', 1000)
# print m
# m.giveRaise(10)
# print m

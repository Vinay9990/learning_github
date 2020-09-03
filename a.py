from abc import ABC, abstractmethod


class Polygon(ABC):

    def noofsides(self):
        pass


class Triangle(Polygon):

    def noofsides(self):
        print("I have 3 sides")


class Pentagon(Polygon):

    def noofsides(self):
        print("I have 5 sides")


class Hexagon(Polygon):

    def noofsides(self):
        print("I have 6 sides")


class Quadrilateral(Polygon):

    def noofsides(self):
        print("I have 4 sides")



R = Triangle()
R.noofsides()

K = Quadrilateral()
K.noofsides()

R = Pentagon()
R.noofsides()

K = Hexagon()
K.noofsides()

from abc import ABC, abstractmethod


class Animal(ABC):
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("I can walk and run")
class Snake(Animal):
    def move(self):
        print("I can crawl")
class Dog(Animal):
    def move(self):
        print("I can bark")
class Lion(Animal):
    def move(self):
        print("I can roar")
R = Human()
R.move()

K = Snake()
K.move()

R = Dog()
R.move()

K = Lion()
K.move()
import abc


class parent:
    def geeks(self):
        pass
class child(parent):
    def geeks(self):
        print("child class")
print(issubclass(child, parent))
print(isinstance(child(), parent))
from abc import ABC, abstractmethod
class R(ABC):
    def rk(self):
        print("Abstract Base Class")
class K(R):
    def rk(self):
        super().rk()
        print("subclass ")

r = K()
r.rk()
import abc
from abc import ABC, abstractmethod


class parent(ABC):
    @abc.abstractproperty
    def geeks(self):
        return "parent class"


class child(parent):

    @property
    def s(self):
        return "child class"
try:
    r = parent()
    print(r.s)
except Exception as err:
    print(err)

r = child()
print(r.s)
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def move(self):
        pass


class Human(Animal):
    def move(self):
        print("I can walk and run")


class Snake(Animal):
    def move(self):
        print("I can crawl")


class Dog(Animal):
    def move(self):
        print("I can bark")


class Lion(Animal):
    def move(self):
        print("I can roar")


c = Animal()


def make_pair(x, y):
    def dispatch(m):
        if m == 0:
            return x
        elif m == 1:
            return y

    return dispatch


class Account(object):
    def __init__(self, holder, number, balance, credit_line=1500):
        self.Holder = holder
        self.Number = number
        self.Balance = balance
        self.CreditLine = credit_line

    def transfer(self, target, amount):
        pass

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

    def balance(self):
        pass
class Greeting:
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print ("Destructor started")
    def SayHello(self):
        print ("Hello", self.name)
class Account(object):
    def __init__(self, holder, number, balance,credit_line=1500):
        self.Holder = holder
        self.Number = number
        self.Balance = balance
        self.CreditLine = credit_line

    def deposit(self, amount):
        self.Balance = amount

    def withdraw(self, amount):
        if(self.Balance - amount < -self.CreditLine):
            # coverage insufficient
            return False
        else:
            self.Balance -= amount
            return True

    def balance(self):
        return self.Balance


class Account(object):
    counter = 0
    def __init__(self, holder, number, balance,credit_line=1500):
        Account.counter += 1
        self.__Holder = holder
        self.__Number = number
        self.__Balance = balance
        self.__CreditLine = credit_line
    def __del__(self):
        Account.counter -= 1

class Account(Counter):
        def __init__(self,
                     account_holder,
                     account_number,
                     balance,
                     account_current=1500):
            Counter.__init__(self)

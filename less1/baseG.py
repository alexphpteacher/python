"""Основы описания классов 5"""

from abc import ABC, abstractmethod

class Named:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name

class Aged:
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return "I am " + str(self.age) + " years old"

class People(Named, Aged):
    def __init__(self, name, age):
        Named.__init__(self, name)
        Aged.__init__(self, age)

    def __str__(self):
        return Named.__str__(self) + " " + Aged.__str__(self)

class SexPeople(People, ABC):
    @abstractmethod
    def getSex(self):
        pass

    def who(self):
        return self.getSex() + " " + self.name

class Man(SexPeople):
    def getSex(self):
        return 'Mr'

class Woman(SexPeople):
    def getSex(self):
        return 'Ms'

if __name__ == "__main__":
    print("""
        m = Man("alex", 22)
        w = Woman("olga", 34)

        print('-'*30)

        print(isinstance(m, Man))
        print(isinstance(m, Woman))
        print(isinstance(m, People))

        print('-'*30)

        print(issubclass(Man, People))
        print(issubclass(Man, Woman))

        print('-'*30)
    """)

    m = Man("alex", 22)
    w = Woman("olga", 34)

    print('-'*30)

    print(isinstance(m, Man))
    print(isinstance(m, Woman))
    print(isinstance(m, People))

    print('-'*30)

    print(issubclass(Man, People))
    print(issubclass(Man, Woman))

    print('-'*30)
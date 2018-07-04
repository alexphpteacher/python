class Human:
    def __init__(self, name, age, weight, height):
        if type(name) == str:
            self.name = name
        else:
            raise Exception("Please, input your name by using string type")

        if type(age) == int:
            self.age = age
        else:
            raise Exception("Please, input your age by using integer type")

        if (type(weight) == float or type(weight) == int) and (
                type(height) == float or type(height) == int):
            self.weight = float(weight)
            self.height = float(height)
        else:
            raise Exception("Please, input your weight and height by using float type")


from abc import ABC, abstractmethod


class Compare(ABC):
    @abstractmethod
    def do_compare(self, obj):
        pass

    def compere(self, obj):
        if isinstance(obj, self):  # если обьект того же класса что и текущий
            return self.do_compare(obj)
        else:
            raise Exception("Sorry, try later")


class HumanComperable(Human, Compare):
    def do_compare(self, obj):
        if self.age > obj.age:
            return 1
        elif self.age == obj.age:
            return 0
        else:
            return -1


class Iterable(ABC):

    def __iter__(self):
        return self.getSequence().__iter__()

    @abstractmethod
    def getSequence(self):
        pass




class A1:
    age = 10
    @classmethod
    def say(cls):
        print(cls.age)

    def __init__(self, age = 11):
        self.age = age

    @staticmethod
    def isAdult(val):
        return val > 18
class A2(A1):
    age = 100

a1 = A1()
a2 = A2()
a22 = A2(22)

a1.say()
a2.say()

print(a2.isAdult(a2.age))
print(a22.isAdult(a22.age))
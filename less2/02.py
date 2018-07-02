class A1:
    i = 10

    @classmethod
    def say(cls):
        return cls.i

    def f(self, number):
        return number +1

    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            setattr(self, k, v)

def my_meta(classname, bases, attrs):
    return A1

class A2(metaclass=my_meta):
    def f(self):
        print('heelo')

a = A2(name = 'alexey', age = 23, phone = '555-789-44-66')

print(vars(a))
print(a.say())

a.f()
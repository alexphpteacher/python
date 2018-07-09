#type(name, bases, attrs)

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

a1 = A1(name = 'alex', age = 12)

print(vars(a1))
print('=' * 60)


def my_say(cls):
    return cls.i

def my_init(self, **kwargs):
    for k, v in kwargs.items():
        setattr(self, k, v)

A2 = type('MyClass',(object,), {
    'i': 11,
    'say': classmethod(my_say),
    'f': lambda n: n +1,
    '__init__': my_init
})

a2 = A2(name = 'alex', age = 12)

print(vars(a2))
print('=' * 60)

print(A1.say())
print(A2.say())
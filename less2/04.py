class A1:
    ff = 10
    def f(self):
        print('f call ' + str(A1.ff))

a1 = A1()

A1.f(A1)
a1.f()

print('='*50)

class Meta(type):
    gg = 11
    def g(cls):
        print('g call ' + str(cls.gg))

class A2(A1, metaclass=Meta):
    pass

a2 = A2()

a2.f()
A2.f(A2)
A2.g()
Meta.g(Meta)


print('='*50)
print(A1.ff)
print(a1.ff)

print(A2.gg)
print(Meta.gg)


a2.g()
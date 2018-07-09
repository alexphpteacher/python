# __call__ , __init__ , __new__


# class A(...):
#   ....

# A = type('A',bases, attrs)

# A = type.__call__('A', base, attrs)
#
#       A = type.__new__(type, 'A', bases, attrs)
#       type.__init__(A, name, bases, attrs)

# class Meta(type):
#   ......
#
#
#
# class A(...,metaclass=Meta):
#   ....

# A = Meta('A',bases, attrs)

# A = Meta.__call__('A', base, attrs)
#
#       A = Meta.__new__(Meta, 'A', bases, attrs)
#       type.__init__(A, 'A', bases, attrs)



class MyMeta(type):
    def __init__(cls, name, bases, attrs):
        print(cls)
        print(name)
        print(bases)
        print(attrs)
        super().__init__(name, bases, attrs)
        cls.f = lambda self: 'hello' + str(self.a)


class A1(metaclass=MyMeta):
    def __init__(self):
        self.a = 10

    def g(self):
        return 'ggg'

a = A1()

print(a.g())
print(a.f())


print(dir(A1))
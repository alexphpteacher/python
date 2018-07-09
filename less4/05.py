class Meta_1(type):
    def __call__(cls, *a, **kw):
        print("entering Meta_1.__call__()")
        rv = super().__call__(cls, *a, **kw)
        print("exiting Meta_1.__call__()")
        return rv
        # return object()

    def __init__(cls, name, bases, attrs):
        print("entering Meta_1.__init__()")
        rv = super().__init__(name, bases, attrs)
        print("exiting Meta_1.__init__()")
        return rv

    def __new__(cls, name, bases, attrs):
        print("entering Meta_1.__new__()")
        rv = super().__new__(cls, name, bases, attrs)
        print("exiting Meta_1.__new__()")
        return rv

class Class_1(object, metaclass=Meta_1):
    def __new__(cls, *a, **kw):
        print("entering Class_1.__new__()")
        rv = super().__new__(cls)
        print("exiting Class_1.__new__()")
        return rv

    def __init__(self, *a, **kw):
        print("entering Class_1.__init__()")
        rv = super().__init__()
        print("exiting Class_1.__init__()")

        for k,v in kw.items():
            setattr(self,k,v)

        self.id = 20
        return rv
    def __call__(cls, *a, **kw):
        print("entering Class_1.__call__()")
        rv = super().__call__(cls, *a, **kw)
        print("exiting Class_1.__call__()")
        return rv

print('='*50)
c = Class_1(name = 'alex', age = 12)

print(dir(c))
print(c.__class__)

print(vars(c))
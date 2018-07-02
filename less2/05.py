class Meta_1(type):
    def __call__(cls, *a, **kw):
        print("entering Meta_1.__call__()")
        rv = super().__call__(cls, *a, **kw)
        print("exiting Meta_1.__call__()")
        return rv

    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)

    def __new__(cls, name, bases, attrs):

        return super().__new__(cls, name, bases, attrs)

class Class_1(object, metaclass=Meta_1):
    def __new__(cls, *a, **kw):
        print("entering Class_1.__new__()")
        rv = super().__new__(cls)
        print("exiting Class_1.__new__()")
        return rv

    def __init__(self, *a, **kw):
        print("executing Class_1.__init__()")
        super().__init__()

        for k,v in kw.items():
            setattr(self,k,v)
        self.a = 10

print('='*50)
c = Class_1(name = 'alex', age = 12)

print(vars(c))
def ff(*a, **bb):
    print('extra action')
    return f(*a, **bb)
#    return f(a[0], a[1], a[2], a[3], **bb)

def f(a,b,c,d):
    print(a)
    print(b)
    print(c)
    print(d)

ff(1,2,3,4)



class A:
    def __init__(self, *args, **kwargs):
        self.list = []
        for k,v in kwargs.items():
            setattr(self, k, v)

        for i in args:
            self.list.append(i)

    def addItem(self, item):
        self.list.append(item)

obj = A(1,2,3,4,5,6,11,111,22, a=10, b= 22, c = 333)

obj.addItem('aa')
obj.addItem('44')
obj.addItem('fff')
obj.addItem('fff1')
obj.addItem('fff2')

print(vars(obj))


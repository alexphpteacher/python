def ff(*a, **bb):
    print('add_files action')
    return f(*a, **b)



class F:
    def __call__(self, a, b, c, d):
        print(a)
        print(b)
        print(c)
        print(d)

ff = F()
def f(a,b,c,d):
    print(a)
    print(b)
    print(c)
    print(d)


g = f
gg = g

gg(1,2,3,4)
gg.__call__(1,2,3,4)
a = 10
print(a)
print(f)

print(dir(f))
print(dir(ff))


def f(g):
    print(g)

    def func():
        print('this is a func', g)

    g += 10
    return func

a1 = f(10)

a1()


def decorate_f(func):
    def decorated_func(*args, **kwargs):
        print('before original functionality')
        result = func(*args, **kwargs)
        print('after original functionality')
        return result

    return decorated_func

def f1(a,b):
    print(a,b)
    return True

@decorate_f
def f2(a,b):
    print(a+b, a*b)
    return True
print('='*50)
print(f1(2,3))
print('='*50)
print(f2(2,3))
print('='*50)

# f1 = decorate_f(f1)
# print(f1(2,3))

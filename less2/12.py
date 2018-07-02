def f1(a,b,c):
    print(a)
    print(b)
    print(c)
    d = a + b + c

def f2(a,b,c):
    print(a)
    print(b)
    print(c)
    d = a + b + c

def ff(func):


    def fr(*args, **kwargs):
        try:
            fff = f2
            fff(*args, **kwargs)
            func(*args, **kwargs)
        except Exception as e:
            print('logging' + str(e))
            raise e
        else:
            print('no error')
        finally:
            print('loggin end')

    func = f2
    return fr

f1(1,2,3)

print('=' * 50)
f1 = ff(f1)

print(dir(f1))
print(f1.__code__)

# f2 = ff(f2)



# print(f1)
# print(f2)
# f1(1,2,3)
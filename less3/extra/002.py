def f1(*args, **kwargs):
    print('args type:', type(args))
    print('kwargs type:', type(kwargs))

    for i,v in enumerate(args):
        print(i, v)

    for k,v in kwargs.items():
        print(k,v)

f1('a','b','c','d', alex= 12, olga=13, inna = 14)
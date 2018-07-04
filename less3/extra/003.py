def f(a, b, c, d, aa, bb, cc, dd):
    print(a,b,c,d)
    print(aa,'',bb,'',cc,'',dd)

args = [1,2,3,4]
kwargs = {
    'aa': 'aa val',
    'bb': 'bb val',
    'cc': 'cc val',
    'dd': 'dd val',
}

f(*args, **kwargs)
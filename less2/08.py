try:
    x = 10
    # x = int([1,2])
    print('x=' + str(x))

    x = [1,2,3,4,5]
    print(x[10])


    x = {}
    # x['value'] = 100
    print(x['value'])


except KeyError:
    print('key error')
except TypeError:
    print('type error')
else:
    print('no error')
finally:
    print('end the end')

print('bye')
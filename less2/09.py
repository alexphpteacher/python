class MyException(Exception):
    def __init__(self, error_message, extra = 'none'):
        super().__init__(error_message)
        self.extra_text = extra

    def ff(self):
        print('class function')

    def __str__(self):
        return super().__str__() + 'extra:' + str(self.extra_text)

def ggg():
    try:
        raise MyException('example error', 'ttttt')
    except MyException as e:
        print('ggg except')
        raise e
    finally:
        print('finally ggg')

try:
    x = 10
    ggg()
    # x = int([1,2])
    print('x=' + str(x))

    # x = [1,2,3,4,5]
    # print(x[10])

    a = MyException('error message', 'my example')

    raise a

    x = {}
    x['value'] = 100
    print(x['value'])
except (KeyError, TypeError) as e:
    print('error:' + str(e))
except MyException as e:
    print(str(e))
    MyException.ff(MyException)
    print('myexception')
except Exception as e:
    print('exception')
    print(str(e))
else:
    print('no error')
finally:
    print('end the end')
print('bye')

MyException.ff(MyException)
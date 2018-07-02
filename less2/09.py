class MyException(Exception):
    def __init__(self, error_message, extra = 'none'):
        super().__init__(error_message)
        self.extra_text = extra

    def __str__(self):
        return super().__str__() + 'extra:' + str(self.extra_text)

try:
    x = 10
    # x = int([1,2])
    print('x=' + str(x))

    # x = [1,2,3,4,5]
    # print(x[10])

    raise MyException('error message', 'my example')


    x = {}
    x['value'] = 100
    print(x['value'])
except (KeyError, TypeError) as e:
    print('error:' + str(e))
except Exception as e:
    print(str(e))
else:
    print('no error')
finally:
    print('end the end')
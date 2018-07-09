class Context:
    def __init__(self, stop_exception):
        self.data = 'some data'
        print('__init__')
        self.stop_exception = stop_exception

    def __enter__(self):
        print('__enter__')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print('__exit__({}, {})'.format(exc_type.__name__, exc_val))
        return self.stop_exception

print('='*50)
with Context(True) as x:
    print(x.data)
    raise RuntimeError('some error')

print('='*50)
with Context(False) as x:
    print(x.data)

print('='*50)
with Context(False) as x:
    print(x.data)
    raise RuntimeError('some error')
print('='*50)

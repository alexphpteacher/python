"""Модуль вычисления чисел Фибоначи"""

a = 'a value'
b = 'b value'

import sub_module

def who_are_you():
    print(__name__)

def get_fib(n):		# get fibonachee numbers
    result = []
    a, b = 0, 1
    while b < n:
	    result.append(b)
	    a, b = b, a+b
    return result

def print_fib(n):		#print fibonachee numbers
    for x in get_fib(n): print(x)

def get_a(): return a
def get_b(): return b

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1 and sys.argv[1].isdigit(): print_fib(int(sys.argv[1]))

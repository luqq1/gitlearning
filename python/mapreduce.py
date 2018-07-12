# -*- coding: utf-8 -*-
from functools import reduce

def normalize(name):
    return name.capitalize()
    # n = 0
    # for c in name:
        # if n == 0:
            # name[i] = name[i].capitalize()
        # else:
            # name[i] = lower(name[i])
    # return name
	
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

def prod(L):
    def f(x, y):
        return x * y
    return reduce(f, L)
	
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': 0}

def str2float(s):
    dot = s.index('.')
    part1 = s[:dot]
    part2 = s[dot+1:]
    part2 = part2[::-1]
    def fn(x, y):
        return x * 10 + y
    def fn1(x, y):
	    return x / 10 + y
    def char2num(s):
        return DIGITS[s]
    d1 = reduce(fn, map(char2num, part1))
    d2 = reduce(fn1, map(char2num, part2))/10
    return d1 + d2

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

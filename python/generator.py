# -*- coding: utf-8 -*-

def triangles():
    list = [1]
    yield list
    list = list[:]
    list.append(1)
    yield list
    n = 1
    while n < 10:
        list = list[:]
        list.insert(1, list[0] + list[1])
        x = 2
        while x <= n:
            list[x] = list[x] + list[x + 1]
            x = x + 1
        yield list
        n = n + 1
    return 'done'


n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
print(results)
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')

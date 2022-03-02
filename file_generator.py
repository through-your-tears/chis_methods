import os

a = int(input('Введите номер задачи: \n'))
n = int(input('Введите кол-во тестов: \n'))
for _ in range(n):
    try:
        f = open(f'tests{a}/test{_}.txt', 'w')
        f.close()
        f = open(f'tests{a}/answer{_}.txt', 'w')
        f.close()
    except FileNotFoundError:
        os.mkdir(f'tests{a}')
        f = open(f'tests{a}/test{_}.txt', 'w')
        f.close()
        f = open(f'tests{a}/answer{_}.txt', 'w')
        f.close()

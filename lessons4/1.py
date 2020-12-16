# Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать,
# ● написать 3 варианта кода (один у вас уже есть),
# ● проанализировать 3 варианта и выбрать оптимальный,
# ● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
# ● написать общий вывод: какой из трёх вариантов лучше и почему.
import timeit
import cProfile

# 1
n = 0


def func(s):
    p = ''
    while s > 0:
        x = s % 10
        p = p + str(x)
        int(x)
        s = s // 10


func(n)

print(timeit.timeit('func(3486)', number=100, globals=globals()))  # 0.00019490000000000132
print(timeit.timeit('func(6972)', number=100, globals=globals()))  # 0.0001919000000000018
print(timeit.timeit('func(13944)', number=100, globals=globals()))  # 0.00023160000000000194
print(timeit.timeit('func(27888)', number=100, globals=globals()))  # 0.0002582000000000001

cProfile.run('func(100_000_000)')


#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       1    0.000    0.000    0.000    0.000 1.py:15(func)
#       1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#       1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 2


def hug_l(n):
    n = str(n)
    n = (n[::-1])


hug_l('3486')

print(timeit.timeit('hug_l(3486)', number=100, globals=globals()))  # 4.200000000000037e-05
print(timeit.timeit('hug_l(6972)', number=100, globals=globals()))  # 3.929999999999906e-05
print(timeit.timeit('hug_l(13944)', number=100, globals=globals()))  # 3.9100000000000246e-05
print(timeit.timeit('hug_l(27888)', number=100, globals=globals()))  # 3.870000000000262e-05

cProfile.run('hug_l(1_000_000)')
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 Hah.py:5(hug_l)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 3
array = []
l = 3486



def rev_list2(l):
    l = str(l)
    for i in l:
        array.append(i)
    return list(reversed(array))


rev_list2(l)
print(timeit.timeit('rev_list2(3486)', number=100, globals=globals()))  # 0.00033270000000000174
print(timeit.timeit('rev_list2(6972)', number=100, globals=globals()))  # 0.0007147999999999981
print(timeit.timeit('rev_list2(13944)', number=100, globals=globals()))  # 0.0011712000000000007
print(timeit.timeit('rev_list2(27888)', number=100, globals=globals()))  # 0.001638999999999998

cProfile.run('rev_list2(1_000_000)')
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 Hah.py:8(rev_list2)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        7    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

from math import pow

_List = []
n = 10
i = 1

while i != n:
    _List.append(pow((1+1/i),i))
    i += 1

print(_List)

Res = sum(_List)

print(Res)
# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

N = 10
_List = []
x = -N

while N != x-1:
    _List.append(x)
    x += 1

res = 1

with open("C:\\Users\\Андрей\\Desktop\\ДЗ GB\\Python GB\\DZ2\\4.txt", 'r') as _File:
    for line in _File:
        res *= _List [int(line)]

print(_List)
print(res)



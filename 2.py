# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

N = 10
_List = []
i = 1
k = 1
while k != N:
    _List.append(i) 
    i = i * k
    k += 1

print(_List)


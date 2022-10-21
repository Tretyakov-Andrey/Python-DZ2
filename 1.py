# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11


def EnterNum ():
    Num = 22.222
    return Num

def Result (Num):
    Res = sum([int(i) for i in str(Num) if i != '.'])
    print(Res)

Result(EnterNum())
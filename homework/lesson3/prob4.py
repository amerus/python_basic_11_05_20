'''
Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
'''

def neg_exponent(x, y):
    y = abs(y)
    if y == 1:
        return 1/x
    else:
        return (1/x * neg_exponent(x, y - 1))

print(neg_exponent(4, -3))

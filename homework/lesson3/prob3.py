'''
Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму
наибольших двух аргументов.
'''

def my_func(a, b, c) -> float:
    lst = [ a, b, c ]
    lst.remove(min(lst))
    return sum(lst)

print(my_func(-7, 5, 4))

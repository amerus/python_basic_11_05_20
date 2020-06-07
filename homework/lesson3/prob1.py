'''
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''

def dev_catch_zero(numerator: float, denominator: float) -> float:
    try:
        result = numerator / denominator
    except ZeroDivisionError as error:
        result = 0
        print("Division by error is not allowed mathematically.")
    return result

try:
    num, den = input("Please, enter numerator and denominator: ").split(' ')
    num = float(num)
    den = float(den)
    division = dev_catch_zero(num, den)
    print(division)
except (ValueError, TypeError) as error:
    print("Please, enter two numbers separated by space.")

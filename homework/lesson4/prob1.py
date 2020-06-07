'''
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения
расчета для конкретных значений необходимо запускать скрипт с параметрами.
'''

from sys import argv

def pay(*args: float) -> float:
    args = args[0]
    hours_worked, hourly_pay, bonus = [ float(x) for x in args[1:] if x.isdigit() ]
    return hours_worked * hourly_pay + bonus

print("Ваш заработок с премией {:.2f} рублей.".format(pay(argv)))

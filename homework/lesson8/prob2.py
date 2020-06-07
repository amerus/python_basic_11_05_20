'''
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой.
'''

class ZeroDiv:
    def __init__(self, denom):
        self.denom = denom
        try:
            if self.denom == 0:
                raise ZeroDivisionError("Zero denominator is not allowed.")
        except ZeroDivisionError as e:
            print(e)

if __name__ == "__main__":
    a = ZeroDiv(0)
    b = ZeroDiv(1)

'''
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
'''


class ComplexNumbers:
    def __init__(self, real_number, imaginary_number):
        self.real_number = real_number
        self.imaginary_number = imaginary_number
        self.result_str = ""

    def __add__(self, other):
        self.result_str = str(self.real_number + other.real_number) + "+" + \
                          str(self.imaginary_number + other.imaginary_number) + "i"
        return ComplexNumbers(*self.result_str.split('+'))

    def __mul__(self, other):
        self.result_str = str(self.real_number * other.real_number - \
                              self.imaginary_number * other.imaginary_number) + "+" + \
                          str(self.real_number * other.imaginary_number + \
                              self.imaginary_number * other.real_number) + "i"
        return ComplexNumbers(*self.result_str.split("+"))

    def __str__(self):
        return str(self.real_number) + "+" + str(self.imaginary_number) + \
               (["i" if str(self.imaginary_number)[-1] != "i" else ""][0])


if __name__ == '__main__':
    a = ComplexNumbers(2, 4)
    print(a)
    b = ComplexNumbers(3, 5)
    print(b)
    c = a + b
    d = a * b
    print("Addition result:", c)
    print("Multiplication result:", d)

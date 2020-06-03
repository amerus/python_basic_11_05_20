'''
Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы методы
перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()),
деление (__truediv__()).Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, у
множение и обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться
округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше
нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих
двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный
метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет
строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет
строку: *****\n*****\n*****.
'''

class Cell:
    def __init__(self, number_of_cells):
        self.number_of_cells = number_of_cells

    def __add__(self, other):
        return Cell(self.number_of_cells + other.number_of_cells)

    def __sub__(self, other):
        if (self.number_of_cells < other.number_of_cells):
            return "Cannot subtract {} because it is larger than {}".format(other.number_of_cells,self.number_of_cells)
        else:
            return Cell(self.number_of_cells - other.number_of_cells)

    def __mul__(self, other):
        return Cell(self.number_of_cells * other.number_of_cells)

    def __truediv__(self, other):
        return Cell(self.number_of_cells // other.number_of_cells)

    def __str__(self):
        return str(self.number_of_cells)

    def make_order(self, in_a_row):
        self.order_str = ""
        self.in_a_row = in_a_row
        if self.number_of_cells % self.in_a_row == 0:
            for i in range(1,(self.number_of_cells / self.in_a_row)+1):
                self.order_str += '*' * self.in_a_row + "\n"
        else:
            for i in range(1,(self.number_of_cells // self.in_a_row)+1):
                self.order_str += '*' * self.in_a_row + "\n"
            self.order_str += '*' * (self.number_of_cells % self.in_a_row) + "\n"
        return self.order_str.strip("\n")


a = Cell(10)
b = Cell(20)
c = a + b
print(c)

a = Cell(10)
b = Cell(20)
c = a - b
print(c)

a = Cell(30)
b = Cell(20)
c = a - b
print(c)

a = Cell(30)
b = Cell(20)
c = a * b
print(c)

a = Cell(35)
b = Cell(20)
c = a / b
print(c)

print(a.make_order(6))
print('-------------')
print(b.make_order(6))

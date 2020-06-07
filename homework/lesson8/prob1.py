'''
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
'''

class Data:

    def __init__(self, my_input: str):
        self.my_input = my_input

    @classmethod
    def date_parser(cls, date):
        day, month, year = date.split('-')
        day = int(day)
        month = int(month)
        year = int(year)
        return day, month, year

    @staticmethod
    def date_validator(date):
        day, month, year = Data.date_parser(date)
        try:
            if day not in [x for x in range(1,31)]:
                raise ValueError("Day should be in the range of 1 through 31")
            elif month not in [x for x in range(1,13)]:
                raise ValueError("Month should be in the range of 1 through 12")
            elif len(str(year)) != 4:
                raise ValueError("Please, enter year as a four digit number")
        except ValueError as e:
            return e
        return [day, month, year]


if __name__ == "__main__":
    a = Data("01-11-1970")
    print(a.date_parser("01-11-1970"))
    print(a.date_validator("01-12-1970"))
    print(a.date_validator("01-13-1970"))
    print(a.date_validator("00-12-1970"))
    print(a.date_validator("01-12-19567"))



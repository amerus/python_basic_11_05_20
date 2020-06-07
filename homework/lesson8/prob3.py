'''
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. Проверить
работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список. Класс-исключение
 должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем
очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
При этом работа скрипта не должна завершаться.
'''

class ValidateInput:

    num_array = [ ]

    def __init__(self, user_input):
        self.user_input = user_input.strip(' ').split(' ')

    def validate_int(self):
        for each_number in self.user_input:
            try:
                if (each_number.isdigit() == False):
                    raise ValueError("Cannot insert non-digit")
                self.num_array.append(float(each_number))
            except ValueError as e:
                print(e)
        return self.num_array

    def __str__(self):
        return self.num_array

if __name__ == "__main__":
    while(True):
        user_input = input("Please, enter a number (or type 'stop' to abort):\t")
        if user_input.strip('') == "stop":
            break
        a = ValidateInput(user_input)
        print(a.validate_int())

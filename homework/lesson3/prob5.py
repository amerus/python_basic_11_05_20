'''
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться
к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение
программы завершается. Если специальный символ введен после нескольких чисел, то вначале
нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
'''

sum = 0.0

def strip_and_yield(in_str):
    """Function, which strips a long space-separated string and yields either its float value, zero,
    or STOP string. Can be used to sum user input."""
    for us in in_str.strip(' ').split(' '):
        if us == '$':
            yield 'STOP'
        try:
            float(us)
            yield float(us)
        except:
            yield float(0)

while(True):
    try:
        user_str = input("Please, enter a series of numbers to get the sum. (In order to abort, enter '$'):\n")
        for value in strip_and_yield(user_str):
            sum += value
    except:
        print ("You chose to abort!")
        break
    finally:
        print("Sum of your numbers is {}".format(sum))

'''
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют
элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
'''

my_list = [7, 5, 3, 3, 2]

input_value = input("Please, enter a digit:\n")
if input_value.isdigit():
    input_value = int(input_value)
    if(input_value in my_list):
        first_time = my_list.index(input_value)
        times_found = my_list.count(input_value)
        my_list.insert(first_time+times_found,input_value)
    else:
       my_list.append(input_value)
       my_list.sort(reverse=True)
    print(my_list)

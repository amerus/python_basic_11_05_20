'''
 Для списка реализовать обмен значений соседних элементов, т.е.
 Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
 При нечетном количестве элементов последний сохранить на своем месте.
 Для заполнения списка элементов необходимо использовать функцию input()
'''

user_list = input("Enter a series of elements separated by spaces:\n")
user_list = user_list.strip(' ').split(' ')
temp = user_list[:]

if len(user_list) % 2 == 0:
    temp[::2], temp[1::2] = temp[1::2], temp[::2]
    print(temp)
else:
     temp.append(user_list[-1])
     temp[::2], temp[1::2] = temp[1::2], temp[::2]
     print(temp[:-1])

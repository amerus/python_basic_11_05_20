'''
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''

filename = "my_file.txt"
out_filename = open(filename, "a", encoding='UTF-8')

while(True):
    user_line = input("Please, enter some text:\n")
    if len(user_line.strip()) == 0:
        out_filename.close()
        break
    else:
        out_filename.write(user_line + "\n")

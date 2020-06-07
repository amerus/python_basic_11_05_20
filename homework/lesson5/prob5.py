'''
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''

file = "my_sum.txt"
line = ' '.join([str(x) for x in range(1,101)])

with open(file, "w", encoding="UTF-8") as out_file:
    out_file.write(line)

with open(file, "r", encoding="UTF-8") as in_file:
    for in_line in in_file.readlines():
        print(sum([float(x) for x in in_line.split(' ')]))

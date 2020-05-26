'''
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
'''

file="my_file.txt"

try:
    in_file = open(file,"r",encoding='UTF-8')
    line_count = 0
    word_count = 0
    for line in in_file.readlines():
        line_count += 1
        word_count += len([x for x in line.strip().split(' ') if x.isalpha()])
    print("There are {} lines and {} words in {}.".format(line_count, word_count, file))
    in_file.close()
except IOError:
    print("No such file")

'''
Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
'''

word_string = input("Enter several words separated by spaces:\n")
for index, value in enumerate(word_string.strip(' ').split(' ')):
    print(index+1, value[:10])

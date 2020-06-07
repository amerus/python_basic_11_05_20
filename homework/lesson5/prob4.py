'''
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
'''

file = "english_numerals.txt"
out_file = open("russian_numerals.txt", "w", encoding='UTF-8')

translation = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре",
}

my_array = []

with open(file, "r", encoding='UTF-8') as my_file:
    for line in my_file.readlines():
        for word in line.strip().split(' '):
            my_array.append(word)

for key, value in translation.items():
    for index, word in enumerate(my_array):
        if word == key:
            out_file.write(translation[key] + " ")
            out_file.write(my_array[index+1] + " ")
            out_file.write(my_array[index+2] + "\n")
out_file.close()

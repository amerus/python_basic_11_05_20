'''
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма
получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
'''

import json

input_file = "firms.txt"
output_file = "profits.txt"
comp_dict = { }
profit_list = []

with open(input_file, "r", encoding="UTF-8") as fin, open(output_file, "w", encoding="UTF-8") as fout:
    for line in fin.readlines():
        line = line.strip().split(' ')
        try:
            comp_dict[line[0]] = int(line[2]) - int(line[3])
        except TypeError:
            print("Malformed database entry")

    average = 0
    count = 0
    for key, value in comp_dict.items():
        if value > 0:
            count += 1
            average = (average + value) / count

    profit_list.append(comp_dict)
    profit_list.append({"average_profit": int(average)})

    fout.write(json.dumps(profit_list))


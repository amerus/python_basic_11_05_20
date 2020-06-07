'''
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить
подсчет средней величины дохода сотрудников.
'''

file = "salary_file.txt"
min_salary = 20000

employees = { }
in_file = open(file, "r", encoding="UTF-8")
for line in in_file.readlines():
    line = line.strip().split(' ')
    employees[line[0]] = line[1]

print(*[x for x in employees.keys() if int(employees[x]) < min_salary])
print("{:.2f}".format(sum([ int(x) for x in employees.values()])/len(employees)))

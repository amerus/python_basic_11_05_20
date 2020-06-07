'''
Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента —
номер товара и словарь с параметрами (характеристиками товара: название, цена, количество,
единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у
пользователя.
'''

features = [ "название", "цена", "количество", "eд" ]
items = { }
database = []
counter = 1

while(True):
    for feature in features:
        item = input("Параметр {}:\n".format(feature))
        if item.isdigit():
            item = int(item)
        items.update({feature:item})
    database.append((counter,items.copy()))
    question = input("Добавить еще одно наименование?\n")
    if(question == "n" or question == "н"):
        break
    else:
        counter += 1
print(database)

items = []

for db in database:
    for item in db[1:2]:
        items.append(list(item.values()))

analytics_database = { }
analytics_products = list(zip(*items))
db_arr = []
for product in analytics_products:
    db_arr.append(list(set(product)))
analytics_database = dict(zip(features, db_arr))
print(analytics_database)

'''
 Пользователь вводит месяц в виде целого числа от 1 до 12.
 Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
 Напишите решения через list и через dict
'''

months = [str(x) for x in range(1,13)]
seasons = [ "winter", "winter", "winter", \
           "spring", "spring", "spring", \
           "summer", "summer", "summer", \
           "fall", "fall", "fall" ]
mon_and_seas = dict(zip(months,seasons))

selection = input("Pick a month as a digit:\n")
print(mon_and_seas[selection])

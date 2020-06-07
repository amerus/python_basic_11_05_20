#1
name = input("Please, enter your name?\n")
print("Your name is",name)

num1 = input("Please, enter first number:\n")
num2 = input("Please, enter second number:\n")

if (num1.isdigit() and num2.isdigit()):
    print("The sum of two numbers is {}".format(int(num1) + int(num2)))

#2
#from datetime import timedelta
seconds = input("Please, enter the total number of seconds:\n")

if (seconds.isdigit()):
    seconds = int(seconds)
#    print(str(timedelta(seconds=seconds)))
    minutes = 0
    hours = 0
    while(seconds >= 60):
        seconds -= 60
        minutes += 1
    while(minutes >= 60):
        minutes -= 60
        hours += 1
    print("{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds))

#3
number = input("Please, enter a number:\n")

if (number.isdigit()):
    number_concat = number
    counter = int(number)
    sum = int(number)
    while counter > 1:
        number_concat = number_concat + number
        sum += int(number_concat)
        counter = counter - 1
    print(sum)

#4
number = input("Please, enter a number:\n")
if (number.isdigit()):
    counter = len(number) - 1
    max = 0
    while counter > 0:
        if max > int(number[counter]):
            max = max
        else:
            max = int(number[counter])
        counter -= 1
    print(max)

#5
gross_profit = input("Please, enter gross profit:\n")
expenses = input("Please, enter your expenses:\n")
if (gross_profit.isdigit() and expenses.isdigit()):
    gross_profit = int(gross_profit)
    expenses = int(expenses)
    net = gross_profit - expenses
    if gross_profit > expenses:
        print("Congratulations, you've made ${} from your business!\nYour profit margin is {:.02f}".format(net,
                                                                                                           net/gross_profit))
        employees = input("How many workers do you have?\n")
        if employees.isdigit():
            print("Your net profit per worker is ${:.02f}".format(net/int(employees)))
    elif gross_profit < expenses:
        print("Keep trying if you can afford it. Currently, your loss is -${}".format(abs(net)))
    else:
        print("Breaking even! Making nothing is better than losing it all!")
#6
a = input("Enter starting value a: ")
b = input("Enter goal value b: ")
if (a.isdigit() and b.isdigit()):
    a = int(a)
    b = int(b)
    counter = 1
    while a < b:
        a = a * 1.1
        counter += 1
    print(counter)
else:
    print("Please, enter valid values for a and b.")

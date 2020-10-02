import re
import math
print("Мітченко Антон Дмитрович\nЛабораторна робота №1\nЗавдання №3\n")
def check_float(text):
    pattern = "^[+-]?([0-9]*[.])?[0-9]+$"
    input_text = input(text)
    while not re.match(pattern, input_text):
        input_text = input("Ви ввели значення, яке не задвольняє умові задачі, будь ласка введіть дійсне значення:")
    return float(input_text)
restart = ""
while not restart == "N":
    x = check_float('Введите значение х:')
    if 0<=x<=1:
        y = x**2-x
    else:
        y=x**2-math.sin(math.pi*x**2)
    print(y)
    restart = ""
    while not (restart == "Y") | (restart == "N"):
        restart = input("чи бажаете повторити операцію (Y/N): ")
        if restart == "Y":
            print("запуск програми знову")
        elif restart == "N":
            print("Дякую за користування")
        else:
            print("Введене вами значення не є коректне") 


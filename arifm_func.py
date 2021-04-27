
# Арифметика через фукцию
what = input('Что делаем? (+, -, *, /):')
a = float(input('Введи первое число: '))
b = float(input('Введи второе число: '))
def func(what, a, b,):
    if what == '+':
        return a + b
    elif what == '-':
        return a - b
    elif what == '*':
        return a * b
    elif what == '/':
        return a / b
    else:
        print('не верные данные')
print('Результат: ' + str(func(what, a, b)))

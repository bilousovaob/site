# +, -, *, /, **, %, унарный минус, округление, Пи

# Арифметика
what = input('Что делаем? (+, -, *, /):')
a = float(input('Введи первое число: '))
b = float(input('Введи второе число: '))
if what == '+':
    с = a + b
    print('Результат: ' + str(с))
elif what == '-':
    с = a - b
    print('Результат: ' + str(с))
elif what == '*':
    с = a * b
    print('Результат: ' + str(с))
elif what == '/':
    с = a / b
    print('Результат: ' + str(с))
else:
    print('не верные данные')








# До тех пор пока while не разлучит нас!
# Необходимо написать функцию с тремя аргументами (А, Б и В), которая будет делать следующее:
#
# Сравнивать аргументы А и Б, если А меньше Б, то увеличивать на инкремент В (прибавлять А к В)
# Полученный результат повторно сравнивать с Б, если все еще меньше Б - повторить предыдущий шаг
# Когда А станет больше Б, вывести радостное сообщение в консоль
# Вся история сравнений также выводится в консоль

a = float(input('Введи первое число: '))
b = float(input('Введи второе число: '))
С = float(input('Введи третье число: '))
def func (a, b, c) :
    while a<b :
        a=a+c
        print(a)
    if a>b :
        print('Ура получилось!!!')
    elif a==b==c :
        print('Начни с начала')


print(func(a, b, С))





__author__ = 'Ваши Ф.И.О.'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

# код пишем тут...
import random

number = random.randint(500, 1000)
print(number)
#int_int = int(input("Введите произвольное целое число от 0 до 10: "))
#i = -1
#1вар
while number != 0:
    digit = number % 10
    print(digit)
    number = number // 10


#2вар
for i in range(0, int_int):
    print(i + 1)
    print("The program is completed successfully")


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

a = int(input("Ведите значение первой переменной А = "))
b = int(input("Ведите значение первой переменной B = "))
print("Меняем местами значение переменных А и В")
c = b - a
a = c + a
print("А = ", a)
b = b - c
print("В = ", b)
print("Программа выполнена успешно")

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет

age = int(input("Введите ваш возрост: "))
if age > 18:
    print("Доступ разрешен")
else:
    print("Извините, пользование данным ресурсом только с 18 лет!")













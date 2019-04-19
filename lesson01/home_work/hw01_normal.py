
__author__ = 'Ваши Ф.И.О.'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

import random

#1 вар
num_ran = str(random.randint(10000, 100000))
#nam_rand = list(a)       #''.join
print(num_ran)
num_max = int(max(num_ran))
print(num_max)
print(type(num_max))

#2 вар
number = random.randint(10000, 100000)
print("Случайное целое число = ",number)
max_number = number%10
number = number//10
while number>0:
    if number%10>max_number:
        max_number = number%10
    number = number//10
print("Максимальная цифра в данном числе = ",max_number)

#3 вар
number = random.randint(10000, 100000)
#m = max([int(i) for i in str(a)])
#i = 0
print(number)
num_str = str(number)
num_max = -1
for i in range(len(num_str)):
    if num_max < int(num_str[i]):
        num_max = int(num_str[i])

print(num_max)
print(type(num_max))

number = random.randint(10000, 100000)
print(number)

i = 0
while number != 0:
    digit = number % 10
    if i < digit:
        i = digit
    number = number // 10
print(i)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

a = int(input('Enter a variable A =  '))
b = int(input('Enter a variable B =  '))
print('The variable A is = ', a, 'The a variable B =  ', b)
print('Change the value of variable')
a = a + b
b = a - b
a = a - b
print('The variable A is =  ', a)
print('The variable B is =  ', b)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

print('Calculate the roots of the square equation')
print('ax**2 + bx + c = 0')
a = int(input('Enter coefficient a =  '))
b = int(input('Enter coefficient b =  '))
c = int(input('Enter coefficient c =  '))
print('Calculata discriminant of the square equation D')
D = b**2-4*a*c
print('D =  ', D)
if D > 0:
    import math
    math.sqrt(4)
    x1 = (-b + math.sqrt(D))/(2 * a)
    x2 = (-b - math.sqrt(D))/(2 * a)
    print('D >0, the equation has two roots, x1 = ', x1, 'x2 = ', x2)
elif D == 0:
    x = -b / (2*a)
    print('D=0, the equation has one root, x =  ', x)
else:
    print('The roots has not')








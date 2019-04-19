# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruct = ["яблоко", "банан", "киви", "арбуз"]
long = len(fruct)
for i in range(long):
    print(str(i+1),".","{:>10}".format(fruct[i]))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
a = ['a', 'f', 'v', 'c', 23, 22, "tt", 7, "qq"]
b = ['f', 'v', 'c', 23, 22, "df"]
c = set(a) - set(b) # но это уже тип - множество
print(c)
print(type(c))

a = ['a', 'f', 'v', 'c', 23, 22, "tt", 7, "qq"]
b = ['f', 'v', 'c', 23, 22, "df"]
for i in b:
    if i in a:
        a.remove(i)
print(a)
print(type(a))

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

from random import randint

num_list = int(input("Ведите количество элементов в списке из целых чисел = "))
list_rand = []
new_list = []
for i in range(num_list):
    list_rand.append(randint(0, 100))
    if list_rand[i] % 2 == 0:
        new_list.append(list_rand[i] / 4)
    else:
        new_list.append(list_rand[i] * 2)

print("Произвольный список целых чисел = ", list_rand)
print("Новый список чисел согласно условиям задания = ", new_list)

list_1 = [89, 87, 44, 64, 30, 75, 3, 67]
new_list = []
last_list = len(list_1)
for i in range(last_list):
    if list_1[i]%2 == 0:
        new_list.append(list_1[i] / 4)
    else:
        new_list.append(list_1[i] * 2)
print(list_1)
print(new_list)

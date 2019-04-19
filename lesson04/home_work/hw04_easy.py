# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

list = [1, 2, 4, 0]
list_new = [i ** 2 for i in list]
print(list_new)
print([i ** 2 for i in list])

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

f1 = ['Абиу', 'Абрикос', 'Авокадо', 'Айва', 'Вампи', 'Вангерия', 'Ваниль']
f2 = ['Абиу', 'Авокадо', 'Айва', 'Вампи', 'Вангерия', 'Ваниль', 'Гандария', 'Генипа', 'Горлянка']
f_new = []
for i in f1:
    for j in f2:
        if i in j:
            f_new.append(i)
print(f_new)
fruc = [i for i in f1 for j in f2 if i in j]
print(fruc)
print([i for i in f1 for j in f2 if i in j])

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random
list_rand = [random.randint(-20, 20) for i in range(40)]
print([i for i in list_rand if i >= 0 if i % 3 == 0 or i % 4 == 0])


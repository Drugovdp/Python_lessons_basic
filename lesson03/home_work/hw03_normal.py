# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
def fibonach():
    f1 = f2 = 1
    dict_new = {}
    fib = []
    for i in range(m + 1):
        k = int(i+1)
        if k < 3:
            f2 = 1
        else:
            f1, f2 = f2, f1 + f2
        dict_new.update({k:f2})
    for i in dict_new:
        if i > n - 1 and i <= m:
            fib.append(dict_new.setdefault(i))
    return fib

n, m = map(int, (input("Вывести диапозон ряда Фибоначчи с n-элемента до m-элемента").split()))
print(tuple(fibonach()))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
   print(origin_list)
   n = len(origin_list)
   for j in range(0, n-1):
      for i in range(0, n-j-1):
         if origin_list[i] > origin_list[i + 1]:
            origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]
      print(j + 1, "- ый проход цикла - ", end=" ")
      print(origin_list)
   return origin_list

sort_list = sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])
print(sort_list)

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

print("Дан список : 'мак', 'просо', 'мак', 'мак', 'просо', 'мак', 'просо', 'просо', 'просо', 'мак'")
el = str(input("Введите элемент, который нужно отфильтровать "))
mixed = ['мак', 'просо', 'мак', 'мак', 'просо', 'мак', 'просо', 'просо', 'просо', 'мак']
list_new = []
for i in mixed:
      if el == i:
         list_new.append(i)

print(list_new)

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def parallelogram(a1, a2, a3, a4):
    import math
    if math.sqrt((a2[0]-a1[0])**2 + ((a2[1]-a1[1])**2)) == math.sqrt((a4[0]-a3[0])**2 + ((a4[1]-a3[1])**2)) and \
            a3[1] - a2[1] == a4[1] - a1[1]:
        return 'Это параллелограмм'
    else:
        return 'Нет, это не параллелограмм'

print("Введите координаты точек")
x1, y1 = map(int, input("Координаты точки А: ").split())
a1 = (x1, y1)
x2, y2 = map(int, input("Координаты точки B: ").split())
a2 = (x2, y2)
x3, y3 = map(int, input("Координаты точки C: ").split())
a3 = (x3, y3)
x4, y4 = map(int, input("Координаты точки D: ").split())
a4 = (x4, y4)

print(a1)
print(a2)
print(a3)
print(a4)

print(parallelogram(a1, a2, a3, a4))




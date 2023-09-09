'''
Задача 18: 
Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.

1 2 3 4 5
6
-> 5

ДЛЯ АВТОТЕСТА
'''
list_1 = [1, 2, 3, 4, 5]
k = 6

m = abs(k - list_1[0])  # модуль числа
number = list_1[0]
for i in range(1, len(list_1)):
    if m > abs(list_1[i] - k):
        m = abs(list_1[i] - k)
        number = list_1[i]
print(number)
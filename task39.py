'''
Задача №39. Решение в группах
Даны два массива чисел. Требуется вывести те элементы
первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит
число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество
элементов во втором массиве. Затем элементы второго массива
Ввод: 
7
3 1 3 4 2 4 12
6
4 15 43 1 15 1
Вывод:
3 3 2 12
'''
import random

print(list_1 := [random.randint(0,9) for i in range(int(input('Введите кол-во элементов: ')))]) 

print(list_2 := [random.randint(0,9) for i in range(int(input('Введите кол-во элементов: ')))])

print('Итоговый список:', lst := [i for i in list_1 if i not in list_2])  # или
# for item in list_1:
#     if item not in list_2:
#         lst.append(item)
#print('Итоговый список:', lst)




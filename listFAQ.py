'''
Список (list) в Python - это упорядоченная коллекция элементов, которая может содержать объекты различных типов данных, 
включая числа, строки, другие списки и многое другое. 
Список является одним из наиболее часто используемых и мощных типов данных в Python.

Списки предоставляют множество методов и операций для работы с данными, 
включая добавление и удаление элементов, сортировку, объединение списков и многое другое. 
Они являются универсальными структурами данных и широко используются в программировании на Python.

Основные характеристики списков:

    Изменяемость: Элементы списка могут быть изменены после создания. Вы можете добавлять, удалять и изменять элементы списка.

    Упорядоченность: Элементы списка имеют определенный порядок, который сохраняется при итерации или доступе к элементам.

    Доступ по индексу: К элементам списка можно обращаться по индексу. Индексация начинается с нуля.

    Итерируемость: Вы можете использовать циклы для перебора элементов списка.

    Используются квадратные скобки: Для создания списка обычно используются квадратные скобки, например, [1, 2, 3].
'''
#Пример списка:
my_list = [1, 2, 3, 'a', 'b']

#Вы можете получить доступ к элементам списка так:
print(my_list[0])  # Выведет 1
print(my_list[3])  # Выведет 'a'

#Вы также можете изменять элементы списка:
my_list[0] = 10
print(my_list)  # Выведет [10, 2, 3, 'a', 'b']


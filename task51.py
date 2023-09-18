'''
Задача №51. Решение в группах
Напишите функцию same_by(characteristic, objects), которая
проверяет, все ли объекты имеют одинаковое значение
некоторой характеристики, и возвращают True, если это так.
Если значение характеристики для разных объектов
отличается - то False. Для пустого набора объектов, функция
должна возвращать True. Аргумент characteristic - это
функция, которая принимает объект и вычисляет его
характеристику.

Ввод:                                       Вывод:
values = [0, 2, 10, 6]                      same
if same_by(lambda x: x % 2, values):
    print(‘same’)
else:
    print(‘different’)
'''


# import random

# print(list_1 := [random.randint(0,10) for _ in range(int(input('Введите кол-во элементов в списке: ')))])
# characteristic = list(filter(lambda x: x % 2 == 0, list_1))
# print(characteristic)
# if len(list_1) != len(characteristic):
#     print('False')
# else: print('True')


from random import randint as ri
print(lst := [1,2,5,9])

def same_by(char, some_list):
    result = list(map(char, some_list))
    #print(result)
    #print(set(result))
    if len(set(result)) == 1:
        return True
    return False

print(same_by(lambda x: x % 2 != 0, lst))

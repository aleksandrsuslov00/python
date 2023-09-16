'''
Задача №43. Решение в группах
Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.

Ввод:            Вывод:
1 2 3 2 3        2
'''
# через словарь

# import random
# print(lst := [random.randint(0,10) for i in range(int(input('Введите кол-во элементов в списке: ')))])
# my_dict = {}
# count = 0
# for i in lst:
#     if i not in my_dict.keys():
#         my_dict[i] = 1
#     else: my_dict[i] += 1

# for key, value in my_dict.items():
#     count += value // 2

# print(count)

import random
print(lst := [random.randint(0,10) for i in range(int(input('Введите кол-во элементов в списке: ')))])


#count = 0
count = sum([lst.count(item)//2 for item in set(lst)])

# for item in set(lst):
#     count += lst.count(item)//2  # 

print(count) 


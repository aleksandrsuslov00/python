'''
Задача №19. Решение в группах
Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K – положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]
Примечание: Пользователь может вводить значения
списка или список задан изначально.
'''
import random
lst = [random.randint(0, 100) for i in range(10)]
print(lst)

shift = int(input('Введите число К: '))

#Первый способ: 
#print(lst[:-shift])
#print(lst[-shift:])

'''
lst = lst[-shift:] + lst[:-shift]
print(lst)
'''

#Второй способ:

for i in range(shift):
    lst.insert(0, lst.pop(-1))
print(lst)    



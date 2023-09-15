'''
Задача №33. Решение в группах
Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1
'''
import random

MIN = 1
MAX = 5
print('Оценки изначально: ', numbers := [random.randint(MIN, MAX) for i in range(int(input('Введите количество оценок: ')))])

def change_numbers(array: list):
    # min_vas = MAX  
    # max_vas = MIN   
    # for i in array:
    #     if i < min_vas:   #3 < 5, 3 == min , 3 > 1 max == 3
    #         min_vas = i
    #     elif i > max_vas:
    #         max_vas = i    
    
    # или использовать встроенные функции мин и мах 

    min_vas = min(array)
    max_vas = min(array) 
    
    for i in range(len(array)):
        if array[i] == max_vas:
            array[i] = min_vas
    #return array     return не обязательно
  
print('Оценки после замены: ', change_numbers(numbers))



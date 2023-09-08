'''
Задача 14: Требуется вывести все целые степени двойки (т.е. числа
вида 2k), не превосходящие числа N.

10 -> 1 2 4 8
'''
N = int(input('Введите число N: '))
count = 1

while count <= N:
    print(count, end=' ')
    if count * 2 > N:
        break
    count = count * 2
    


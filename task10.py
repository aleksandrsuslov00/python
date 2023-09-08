'''
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
решкой, а некоторые – гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были
повернуты вверх одной и той же стороной. Выведите минимальное
количество монет, которые нужно перевернуть.

5 -> 1 0 1 1 0
2
'''

import random
coins = int(input('Количество монет на столе: '))

avers_count = 0 #считает орлы
revers_count = 0 #считает решки

for i in range(coins):
    coin = random.randint(0,1)
    print(coin, end=" ")
    if coin == 0:
        avers_count += 1
    else: revers_count += 1

print(f'\nОрлы: {avers_count} шт., решки: {revers_count} шт.')

if avers_count >= revers_count:
    if revers_count == 0: #для случая, когда 1 или 2 монеты и выпали только орлы, а решек 0
       print(f'Нужно перевернуть {avers_count} монет с орлом.') 
    else: print(f'Нужно перевернуть {revers_count} монет с решкой.')
if revers_count > avers_count:
    if avers_count == 0: #для случая, когда 1 или 2 монеты и выпали только решки, а орлов 0
        print(f'Нужно перевернуть {revers_count} монет с решкой.')
    else: print(f'Нужно перевернуть {avers_count} монет с орлом.')    

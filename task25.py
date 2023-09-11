'''
Задача №25. Решение в группах
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию
.split()
'''

#12343456342
#1 2 3 4 3_1 4_1 5 6 3_2 4_2 2_1

#n = str(input('Введите символы строки: '))

some_string = input("Add string: ")

dict_count = {}
result_list = []

for i in some_string:
    if i in dict_count:
        dict_count[i] = dict_count.get(i) + 1
    else:
        dict_count[i] = 1
    if dict_count.get(i) > 1:
        result_list.append(f'{i}_{dict_count.get(i) - 1} ')
    
    else: result_list.append(i)
print(*result_list)
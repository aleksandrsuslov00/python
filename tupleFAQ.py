'''
tuple: 

Кортеж (tuple) в Python - это упорядоченная и неизменяемая коллекция элементов. Кортежи очень похожи на списки, 
но с одним важным отличием: после создания кортежа вы не можете изменить его содержимое - добавлять, удалять или изменять элементы.

Основные характеристики кортежей:

    Неизменяемость: Элементы кортежа не могут быть изменены после создания. Вы можете создать новый кортеж с измененными значениями, 
    но не можете изменить значения внутри существующего кортежа.

    Упорядоченность: Элементы кортежа имеют определенный порядок, который сохраняется при итерации или доступе к элементам.

    Доступ по индексу: К элементам кортежа можно обращаться по индексу, так же как и к элементам списка.

    Итерируемость: Вы можете использовать циклы для перебора элементов кортежа.

    Используются круглые скобки: Для создания кортежа обычно используются круглые скобки, например, (1, 2, 3).


Вы можете получить доступ к элементам кортежа так: '''
my_tuple = (1, 2, 3, 'a', 'b')
print(my_tuple[0])  # Выведет 1
print(my_tuple[3])  # Выведет 'a'

'''
Кортежи полезны, когда вам нужна коллекция данных, которую вы не планируете изменять, например, 
координаты точки на плоскости (x, y) или дни недели ('Понедельник', 'Вторник', ...). 
Они также могут быть использованы в качестве ключей для словарей, так как являются хешируемыми.
'''
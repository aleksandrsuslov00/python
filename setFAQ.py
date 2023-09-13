'''
В Python, set - это класс данных, представляющий множество. Множество является неупорядоченной коллекцией уникальных элементов. Основные характеристики множеств в Python:

    Уникальность элементов: Множество не может содержать дублирующиеся элементы. Если вы попытаетесь добавить элемент, который уже существует в множестве, он не будет добавлен.

    Неупорядоченность: Элементы множества не имеют определенного порядка, и доступ к элементам не осуществляется по индексам.

    Изменяемость: Вы можете добавлять и удалять элементы из множества.

    Используются фигурные скобки: Для создания множества обычно используются фигурные скобки, например, {1, 2, 3}.
'''

#Пример множества:
my_set = {1, 2, 3, 3, 4, 5}

#В результате создания my_set будет содержать только уникальные значения, поэтому дублирующиеся элементы, такие как 3, будут проигнорированы.

#Вы можете выполнять операции над множествами, такие как объединение, пересечение и разность:
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1.union(set2)  # Объединение множеств
intersection_set = set1.intersection(set2)  # Пересечение множеств
difference_set = set1.difference(set2)  # Разность множеств

#Множества полезны в различных сценариях, например, для удаления дубликатов из списка, проверки наличия элементов в коллекции и других задач, где важна уникальность элементов.

print(set1,set2)
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))

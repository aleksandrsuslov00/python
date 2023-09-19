'''
Задача №49. Решение в группах
Планеты вращаются вокруг звезд по эллиптическим орбитам.
Назовем самой далекой планетой ту, орбита которой имеет
самую большую площадь. Напишите функцию
find_farthest_orbit(list_of_orbits), которая среди списка орбит
планет найдет ту, по которой вращается самая далекая
планета. Круговые орбиты не учитывайте: вы знаете, что у
вашей звезды таких планет нет, зато искусственные спутники
были были запущены на круговые орбиты. Результатом
функции должен быть кортеж, содержащий длины полуосей
эллипса орбиты самой далекой планеты. Каждая орбита
представляет из себя кортеж из пары чисел - полуосей ее
эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
где a и b - длины полуосей эллипса. При решении задачи
используйте списочные выражения. Подсказка: проще всего
будет найти эллипс в два шага: сначала вычислить самую
большую площадь эллипса, а затем найти и сам эллипс,
имеющий такую площадь. Гарантируется, что самая далекая
планета ровно одна
Пример ввода и вывода данных представлены на
следующем слайде

Ввод:
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
Вывод:
2.5 10
'''

# import math

# print(list_1 := list(tuple(random.randint(1,10) for i in range(10))))
# print(list_2 := list(tuple(random.randint(1,10) for i in range(10))))
# print(list_3 := set(filter(lambda x: x[0] != x[1], zip(list_1, list_2))))

# print(max_planet := max(map(lambda x: x[0] * x[1]*math.pi, list_3)))

from random import randint as ri

print(planets := [(ri(1,10), ri(1,10)) for _ in range(10)])
planets = set(filter(lambda x: x[0] != x[1], planets))

#print(max(planets, key = lambda x: x[0] * x[1]))
planets = [(planet, planet[0]*planet[1])for planet in planets]
print(max(planets, key = lambda x: x[1])[0])
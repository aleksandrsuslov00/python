'''
Задача 26: Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую степень B с
помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
'''
a = int(input('Введите число А: '))
b = int(input('Введите число Б: '))

def exponentiation(n, m):   #    n - число, m - шаг
    if m == 0:
        return 1
    return n * exponentiation(n, m - 1)  # n * n * n * ... (- 1 шаг каждый повтор)
    

print(exponentiation(a, b))


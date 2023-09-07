'''
Задача №9. Решение в группах
По данному целому неотрицательному n вычислите
значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
чисел от 1 до N) 0! = 1 Решить задачу используя цикл
while
Input: 5
Output: 120 


n = int(input("введите число N: "))
fact = 1
while n > 1:
    fact = fact * n
    n = n - 1
    print(fact)
'''
n = int(input("введите число N: "))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print(fact)


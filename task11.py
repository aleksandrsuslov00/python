'''
Задача №11. Решение в группах
Дано натуральное число A > 1. Определите, каким по
счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не
является числом Фибоначчи, выведите число -1.
Input: 5
Output: 6
'''
n = int(input("введите число N: "))
fib1 = 0
fib2 = 1
count = 1
while fib2 < n:
    fib1,fib2 = fib2, fib1 + fib2
    '''print(fib2)'''
    count += 1
if fib2 == n:
    print(count)
elif n == 1 or n == 0:
    print(n)
else:
    print(-1)

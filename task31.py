'''
Задача №31. Решение в группах
Последовательностью Фибоначчи называется последовательность чисел 
a0, a1, ..., an, ..., где a0 = 0, a1 = 1, ak = a(k-1) + a(k-2) (k > 1).
Требуется найти N-е число Фибоначчи
Input: 8
Output: 21
Задание необходимо решать через рекурсию
'''
def fib(n):
    if n in [1, 2]:            
        return 1
    return fib(n - 1) + fib(n - 2)

list_fib = []
for i in range(1, 10):
    list_fib.append(fib(i))
 


print(fib(int(input('Введите число N: '))))
print(list_fib)
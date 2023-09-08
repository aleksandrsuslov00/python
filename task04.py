'''
Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали n журавликов.

Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

Выведите кортеж из количества журавликов, сделанных Петей, Катей и Сережей.
'''

n = int(input("введите число журавликов: "))

# Пусть Петя сделал a журавликов,
# тогда Сережа сделал b == a журавликов,
# а Катя сделала c == 4a

Peter = n//6
Sergey = Peter
Kate = Peter * 4

print(Peter, Kate, Sergey)
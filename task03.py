
#В некоторой школе решили набрать три новых
#математических класса и оборудовать кабинеты для
#них новыми партами. За каждой партой может сидеть
#два учащихся. Известно количество учащихся в
#каждом из трех классов. Выведите наименьшее
#число парт, которое нужно приобрести для них.

#Input: 20 21 22(ввод чисел НЕ в одну строку)
#Output: 32

a = int(input("Введите кол-во учащихся, 1 класс: "))
b = int(input("Введите кол-во учащихся, 2 класс: "))
c = int(input("Введите кол-во учащихся, 3 класс: "))

#print(((a + b + c) % 2)+(a + b + c) // 2)

total_desks = (a+1)//2 + (b+1)//2 + (c+1)//2

print(total_desks)

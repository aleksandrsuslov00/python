'''
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
школьница. Петя помогает Кате по математике. Он задумывает два
натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
этого Петя делает две подсказки. Он называет сумму этих чисел S и их
произведение P. Помогите Кате отгадать задуманные Петей числа.
'''

sum = int(input('Сумма натуральных чисел: '))
product = int(input('Произведение натуральных чисел: '))

for number_x in range(1, 1000):
    number_y = sum - number_x
    if number_x <= number_y and number_x * number_y == product:
        print(number_x, number_y)      
'''
Задача №27. Общее обсуждение
Пользователь вводит текст(строка). Словом считается
последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом
пробелов или символами конца строки.Определите,
сколько различных слов содержится в этом тексте.
Input: She sells sea shells on the sea shore; The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore, I'm sure that the shells are sea shore shells.
Output: 19
'''
import string

some_text = input('Введите текст: ').lower()
for ch in string.punctuation:
    some_text = some_text.replace(ch, ' ')
some_text = some_text.split()
print(len(set(some_text)))
print(some_text)

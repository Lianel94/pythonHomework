""" Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
*Пример:*
5
1 2 3 4 5
3
-> 1 """
import random

num = int(input("Type the number of elements in the array: "))
arr = []
count = 0
for i in range(num):
    arr.append(random.randint(1, 10))

print(arr)

user_num = int(input("type the number you want to count: "))
for i in arr:
    if user_num == i:
        count += 1

# arr.count(user_num)

print(count)


""" Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
*Пример:*
5
1 2 3 4 5
6
-> 5 """

n = int(input("Type the number of elements in the array: "))
array = []
for i in range(n):
    array.append(random.randint(1, 10))
print(array)

x = int(input("Type the number: "))
close_num = array[0]

for i in array:
    if abs(x - i) < abs(x - close_num):
        close_num = i
print(f"The closest number is {close_num}")


""" *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
*Пример:*
ноутбук
12 """

eng_alphabet = {1: 'AEIOULNSTR',
                2: 'DG',
                3: 'BCMP',
                4: 'FHVWY',
                5: 'K',
                8: 'JX',
                10: 'QZ'}
rus_alphabet = {1: 'АВЕИНОРСТ',
                2: 'ДКЛМПУ',
                3: 'БГЁЬЯ',
                4: 'ЙЫ',
                5: 'ЖЗХЦЧ',
                8: 'ШЭЮ',
                10: 'ФЩЪ'}

lang = input("Type the language eng or rus: ")
user_word = input("Type your word/Напишите ваше слово: ").upper()
sum = 0

if lang == 'rus':
    for i in user_word:
        for (k, v) in rus_alphabet.items():
            if i in v:
                sum += k
elif lang == 'eng':
    for i in user_word:
        for (k, v) in eng_alphabet.items():
            if i in v:
                sum += k
print(sum)

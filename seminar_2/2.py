""" Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть """

num = int(input("Type the number of coins: "))
heads = 0
tails = 0
for i in range(num):
    coin = int(input("0 or 1 where o - tail, 1 - head: "))
    if coin == 0:
        heads += 1
    else:
        tails += 1
if heads > tails:
    print(tails)
elif heads == tails:
    print(tails)
else:
    print(heads)

""" Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа. """



""" Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N. """
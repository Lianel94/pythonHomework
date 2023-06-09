""" Задача No45. Решение в группах
Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа получает на вход одно натуральное число k, не превосходящее 105. Программа должна вывести все пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
Ввод: Вывод:
300 220 284 """

k = int(input("Type the number: "))

def sum_of_div(k):
    sum = 0
    for i in range(1, k):
        if k % i == 0:
            sum += i
    return sum

# print(sum_of_div(k))

def get_friendly_num(k):
    res = []
    for i in range(1, k):
        if i not in res:
            temp = sum_of_div(i)
            if i == sum_of_div(temp) and i != temp:
                res.append(i)
                res.append(temp)
    return res

print(get_friendly_num(k))


""" Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки. """

a1 = int(input("Type the first element: "))
d = int(input("Type the difference: "))
n = int(input("Type the number of the elements: "))

for i in range(n):
    print(a1 + i * d)


# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
""" Ввод: [-5, 9, 0, 3, -1, -2, 1,
4, -2, 10, 2, 0, -9, 8, 10, -9,
0, -5, -5, 7]
Вывод: [1, 9, 13, 14, 19] """

arr = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_idx = int(input("Type the minimum: "))
max_idx = int(input("Type the maximum: "))
for i in range(len(arr)):
    if min_idx <= arr[i] <= max_idx:
        print(i)
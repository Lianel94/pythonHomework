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
    arr.append(random.randint(1,10))

print(arr)

user_num = int(input("type the number you want to count: "))
for i in arr:
    if user_num == i:
        count += 1

print(count)


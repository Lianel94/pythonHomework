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




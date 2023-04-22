""" Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах. Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств
11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18
6 12
"""
import random

num1 = int(input("Type the number of elements for the 1st array: "))
num2 = int(input("Type the number of elements for the 2nd array: "))

array1 = []
array2 = []
ar1_ar2 = []

for i in range(num1):
    array1.append(random.randint(1, 15))
print(array1)

for i in range(num2):
    array2.append(random.randint(1, 20))
print(array2)

for i in array1:
    if i in array2:
        ar1_ar2.append(i)
        ar1_ar2.sort()

print(set(ar1_ar2))





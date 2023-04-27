""" Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
*Пример:*
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8  """

num = int(input("Type the number: "))
pow = int(input("Type the pow: "))

def num_to_pow(num, pow):
    if pow == 0:
        return 1
    return num * num_to_pow(num, pow - 1)

print(num_to_pow(num, pow))


""" Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
*Пример:*
2 2
4  """

num1 = int(input("Type the first positive number: "))
num2 = int(input("Type the second positive number: "))


def sum(num1, num2):
    if num2 == 0:
        return num1
    return sum(num1 + 1, num2 - 1)

print(sum(num1, num2))

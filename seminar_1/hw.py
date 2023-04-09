""" Задача 2: Найдите сумму цифр трехзначного числа.
*Пример:*
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) | """

number = int(input("Type the 3-digit number: ")) #125
print(f"The sum of the digits in the number {number} is {number%10 + number%100//10 + number//100}")


""" Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
*Пример:*
6 -> 1  4  1
24 -> 4  16  4
60 -> 10  40  10 """

birdNum = int(input("Type the number of the paper birds: "))
petya_or_serezha = birdNum // 3 // 2
katya = petya_or_serezha * 2 * 2
print(f"Katya made {katya} paper birds, Petya made {petya_or_serezha} paper birds, and Serezha made {petya_or_serezha} paper birds")


""" Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
*Пример:*
385916 -> yes
123456 -> no """

ticketNum = input("Type the ticket number: ")

if int(ticketNum[0]) + int(ticketNum[1]) + int(ticketNum[2]) == int(ticketNum[3]) + int(ticketNum[4]) + int(ticketNum[5]):
    print("You're lucky. Congratulations!")
else:
    print("Sorry. Maybe next time")



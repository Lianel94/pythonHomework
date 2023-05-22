""" Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
*Пример:*
**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
    **Вывод:** Парам пам-пам   """

vinnie_song = 'пара-ра-рам рам-пам-папам па-ра-па-пам'.split()
arr = []
vowels = ['ё', 'у', 'е', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю']

def isRhyme(str):
    for phrase in vinnie_song:
        syllable = 0
        for i in phrase:
            if i in vowels:
                syllable += 1
        arr.append(syllable)
    return len(arr) == arr.count(arr[0])

if isRhyme(vinnie_song):
    print('Парам пам-пам')
else:
    print('Пам парам')




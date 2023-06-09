# 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

# 5 -> 1 0 1 1 0 
# 2

# 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

# 4 4 -> 2 2
# 5 6 -> 2 3

# 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.

# 10 -> 1 2 4 8

task = input("Введите номер задачи(10, 12, 14): ")

match task.split():
    case ["10"]:
        print("Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.\nОпределите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были\nповернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть\n\n5 -> 1 0 1 1 0 \n2\n")
        cases = int(input("Введите количество случаев: "))

        while cases < 1:
            print("Такого количества эксперементов не может быть!")
            cases = int(input("Введите корректное количество случаев: "))

        countCase0 = 0  # Орёл
        countCase1 = 0  # Решка

        for i in range(cases):
            experiment = int(input(f"Введите результат случая {i+1}, где 0 - это орёл, а 1 - это решка: "))
            while (experiment != 1 and experiment !=0):
                experiment = int(input(f"Введите результат случая {i+1} корректно, где 0 - это орёл, а 1 - это решка: "))
            if experiment == 0:
                countCase0 += 1
            else:
                countCase1 += 1

        if (countCase1 == 0 and countCase0 != 0):
            print(f"Все эксперементы закончились случаем орёл, ничего переворачивать не нужно")
        elif (countCase0 == 0 and countCase1 != 0):
            print(f"Все эксперементы закончились случаем решка, ничего переворачивать не нужно")
        elif countCase0 == countCase1:
            print(f"Нужно перевернуть все решеки, либо все орлы в количестве {countCase1}")
        elif countCase0 > countCase1:
            print(f"Нужно перевернуть {countCase1} решек")
        else:
            print(f"Нужно перевернуть {countCase0} орлов")

    case ["12"]:
        print("Петя и Катя – брат и сестра. Петя – студент, а Катя –\nшкольница. Петя помогает Кате по математике. Он задумывает два\nнатуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для\nэтого Петя делает две подсказки. Он называет сумму этих чисел S и их\nпроизведение P. Помогите Кате отгадать задуманные Петей числа.\n\n4 4 -> 2 2\n5 6 -> 2 3\n")
        import math

        S = int(input("Введите сумму чисел (X + Y): "))
        P = int(input("Введите произведение чисел (X * Y): "))

        # X + Y = S      X = S - Y
        # X * Y = P      P = (S - Y) * Y

        # P = S * Y - 2 * Y
        # P = Y * (S - Y)
        # P = S * Y - Y^2
        # Y^2 - S * Y + P = 0

        D = S * S - 4 * P

        if D < 0:
            print("Подсказки даны неверно!")
        elif D == 0:
            X = Y = S/2
            print(f"{S} {P} -> {Y} {X}")
        else:
            X = (S + math.sqrt(D))/2
            Y = (S - math.sqrt(D))/2
            print(f"{S} {P} -> {Y} {X}")

    case ["14"]:
        print("14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.\n\n10 -> 1 2 4 8\n")
        N = int(input("Введите число N: "))

        result = 1

        print(f"{N} ->", end = " ")

        while N > result:
            print(result, end = " ")
            result *= 2

    case _:
        print("Введён некорректный номер задачи!")
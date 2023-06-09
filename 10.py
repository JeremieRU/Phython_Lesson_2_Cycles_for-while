# 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

# 5 -> 1 0 1 1 0 
# 2

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
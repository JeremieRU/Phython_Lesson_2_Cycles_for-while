# 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.

# 10 -> 1 2 4 8

N = int(input("Введите число N: "))

result = 1

print(f"{N} ->", end = " ")

while N > result:
    print(result, end = " ")
    result *= 2
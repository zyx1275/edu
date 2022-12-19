# Задайте список из n чисел последовательности (1+(1/n))**n и выведите на экран их сумму.

N = int(input("Укажите число: "))
result = {}

for i in range(1, N+1):
    calculate_result = (1+(1/i))**i
    result[i] = round(calculate_result, 2)

print(result)
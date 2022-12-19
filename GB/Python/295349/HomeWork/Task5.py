# Реализуйте алгоритм перемешивания списка.
from random import randint


N = int(input("Укажите размер массива: "))
cur_pos = 0
new_pos = 0
orig_array = []

# Заполняем массив случайными числами от 10 до 99 включительно
print("Оригинальный массив:")
for i in range(N):
    x = randint(10,99)
    orig_array.append(x)
print(orig_array)

print()

# выполняем перемещение в массиве столько раз, сколько в нем цифр
print("Перемешенный массив")
for i in range(N):

    # Если текущий индекс и новый индекс совпали - генерируем новый индекс еще раз
    while True:
        new_pos = randint(0, N-1)
        if new_pos != cur_pos:

            # меняем содержимое элементов массива между cur_pos и new_pos
            tmp = orig_array[new_pos]
            orig_array[new_pos] = orig_array[cur_pos]
            orig_array[cur_pos] = tmp

            # меняем индексы местами
            cur_pos, new_pos = new_pos, cur_pos
            break
print(orig_array)

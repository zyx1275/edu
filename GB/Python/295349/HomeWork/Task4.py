# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

N = int(input("Укажите число: "))
list = []
summ = 1

# заполняем список
for i in range(-N,N+1):
    list.append(i)

# читаем данные из файла
f_path = "file.txt"
f = open(f_path, "r")
for line in f:

    # пропускаем число, если оно больше последнего индекса массива
    x = int(line)
    if x > N-1: continue
    
    summ *= x

f.close()

print(list)
print(summ)
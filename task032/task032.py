# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
#
# Диапазон от 6 до 12
#
# Вывод: [1, 9, 13, 14, 19]
import random


def gen_array(arr_len):
    arr = []
    for i in range(arr_len):
        arr.append(random.randint(-10, 10))
    return arr


array = gen_array(random.randint(6, 25))
print(f'Дан массив: \n{array}')

start = int(input('Введите начало диапазона искомых значений:\n'))
end = int(input('Введите конец диапазона искомых значений:\n'))
res = []

if start or end not in array:
    print('Заданных значений нет в массиве\n')
else:
    for i in range(len(array)):
        if start <= array[i] <= end:
            res.append(i)
print(f'Индексы, содержащие значения в диапазоне от {start} до {end}:\n{res}')


# В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по
# окружности. Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод —
# на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.
import random


# Генерируем грядку
def gryadka_gen(n):
    gr = list()
    for i in range(n):
        gr.append(kust_gen(random.randint(3, 12)))
    #print(f'Грядка {gr}')
    return gr


# Генерируем куст
def kust_gen(n):
    kust = random.randint(10, 100)
    return kust


# Модуль подсчета ягод
def collecting_berrys_module(grdk, kust_index):
    if len(grdk) < 3:
        print('Должно быть не меньше 3 кустов!')
        return -1
    if kust_index > len(grdk) - 1:
        print('Переданный индекс за пределами грядки!')
        return -2
    berry_quantity = 0
    berry_quantity += grdk[kust_index - 1] + grdk[kust_index]
    if kust_index == len(grdk) - 1:
        berry_quantity += grdk[0]
    else:
        berry_quantity += grdk[kust_index + 1]
    return berry_quantity


gryadka = gryadka_gen(random.randint(6, 8))
print(f'Сгенерирована грядка: {gryadka}')

select_kust = random.randint(0, len(gryadka)-1)

print(f'Для сбора выбран куст по индексу {select_kust}, его значение = {gryadka[select_kust]}')


berrys = collecting_berrys_module(gryadka, select_kust)

print(f'С куста по индексу {select_kust} и двух его соседей (слева и справа) собрано {berrys} ягод\n')

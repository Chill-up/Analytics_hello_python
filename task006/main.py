# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
#
# *Пример:*
#
# 385916 -> yes
# 123456 -> no
import random

bilet_number = random.randrange(100000, 999999) #рандомно выдаем номера
#bilet_number = 385916 #номер для проверки

print(f'Ваш номер билета: {bilet_number}!')

left_side_sum = 0
right_side_sum = 0

while bilet_number > 0:
    if bilet_number >= 1000:
        right_side_sum += bilet_number % 10
        bilet_number = bilet_number // 10
    else:
        left_side_sum += bilet_number % 10
        bilet_number = bilet_number // 10

if right_side_sum == left_side_sum:
    print('Ура! Вам достался счастливый билет!')
else:
    print('Вам достался обычный билет. Повезет в другой раз!')

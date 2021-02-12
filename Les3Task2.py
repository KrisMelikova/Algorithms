#Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
first_array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(first_array)
second_array = []

for i, item in enumerate(first_array):
    if item % 2 == 0:
        second_array.append(i)

my_string = ','.join(str(e) for e in second_array)
print(f'Индексы четных элементов первого массива: {my_string}')
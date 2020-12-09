#В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Исходный массив: {array}')

maximum = array[0]
minimum = array[0]

for i in array:
    if i > maximum:
        maximum = i
    if i <= minimum:
        minimum = i
a = array.index(maximum) #индекс максимального элемента
b = array.index(minimum) #индекс минимального элемента

print(f'Максимальное число {maximum}, его индекс {a}')
print(f'Минимальное число {minimum}, его индекс {b}')


array[a], array[b] = array[b], array[a]

print(f'В массиве поменяли местами минимальный и максимальный элементы: {array}')
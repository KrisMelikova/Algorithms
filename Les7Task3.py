# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой — не больше медианы.

import random

def gnome(arr):
    i, j, size = 1, 2, len(arr)
    while i < size:
        if arr[i - 1] <= arr[i]:
            i, j = j, j + 1
        else:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            i -= 1
            if i == 0:
                i, j = j, j + 1
    return arr

m = int(input('Введите натуральное число'))
n = 2 * m + 1
array = [random.randint(0, n) for i in range(n)]

print('Исходный массив:', array)
print(gnome(array))

mid = len(array) // 2
print('Медиана:', array[mid])



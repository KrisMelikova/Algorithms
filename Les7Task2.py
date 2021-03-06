# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

def merge_sort(arr):  # в этой функции делаем саму сортировку
    if len(arr) == 1:  # если длина списка будет равна 1, то считаем, что он отсортирован
        return arr
    mid = len(arr) // 2  # находим середину списка
    left = merge_sort(arr[:mid])  # применяем рекурсию на получившуюся левую часть
    right = merge_sort(arr[mid:])  # применяем рекурсию на получившуюся правую часть
    return merge_lists(left, right)


def merge_lists(one, two):  # в этой функции делаем слияние
    i = 0  # первый указатель
    j = 0  # второй указатель
    my_list = []
    while i < len(one) and j < len(two):
        if one[i] < two[j]:  # сравниваем элементы списков, в зависимости от того, кто меньше, кладем в my_list
            my_list.append(one[i])
            i += 1  # если клали i - элемент, то двигаем указатель вправо (то есть делаем +1)
        else:
            my_list.append(two[j])
            j += 1  # если клали j - элемент, то двигаем указатель вправо (то есть делаем +1)
    if i < len(one):  # в каком-то списке еще могли остаться элементы, поэтому остатки мы добавляем в my_list
        my_list += one[i:]
    if j < len(two):
        my_list += two[j:]
    return my_list  # и возвращаем полученный список


array = [45.1, 7.0, 17.4, 13.8, 7.4, 19.8, 22.3, 1.7, 4.0, 36.8, 25.7, 8.0, 0.0, 9.0, 47.8, 27.6, 3.5, 5.0, 0.6, 38.8,
         20.5, 13.9, 34.5, 3.3, 16.2, 36.5, 45.6, 40.7, 47.1, 45.0, 48.5, 45.4, 47.9, 23.4, 20.1, 14.4, 3.4, 6.7, 7.7,
         18.0, 13.5, 29.1, 44.5, 40.3, 44.3, 32.2, 30.7, 47.4, 3.8, 39.9, 8.4, 25.4, 18.9, 31.0, 14.2, 10.1, 43.6, 41.3,
         43.7, 35.3, 35.8, 19.9, 41.2, 3.9, 40.2, 2.2, 17.5, 40.5, 4.4, 49.3, 6.0, 19.0, 39.6, 29.2, 44.4, 25.9, 2.9,
         48.3, 24.9, 37.0, 15.3, 45.5, 32.9, 7.8, 18.4, 4.6, 1.0, 40.6, 48.6, 34.0, 27.1, 6.1, 17.2, 6.4, 27.4, 23.6,
         37.7, 32.4, 41.0, 36.6, 26.7, 30.1, 47.7, 20.7, 45.7, 1.8, 18.2, 2.7, 32.8, 38.1, 31.1, 26.1, 39.4, 8.8, 33.0,
         36.0, 3.2, 36.1, 15.7, 37.4, 2.1, 5.9, 17.3, 37.9, 27.0, 14.0, 24.5, 10.0, 18.1, 23.8, 39.3, 47.2, 39.7, 3.6,
         4.5, 48.8, 1.2, 31.8, 38.7, 0.2, 44.1, 6.3, 45.8, 4.3, 10.3, 3.7, 22.6, 21.3, 28.0, 9.5, 19.7, 24.0, 5.3, 30.6,
         43.3, 1.6, 18.3, 8.9, 36.2, 28.9, 38.0, 26.5, 36.7, 49.2, 18.6, 31.6, 27.3, 16.5, 41.7, 9.2, 18.5, 34.3, 43.8,
         1.5, 11.3, 17.8, 35.7, 29.7, 4.2, 19.5, 43.5, 9.3, 46.0, 29.9, 7.1, 16.7, 39.8, 37.5, 12.7, 16.9, 16.6, 23.0,
         39.1, 21.2, 17.6, 19.1, 49.9, 8.7, 2.0, 46.6, 0.8, 34.4, 48.2, 41.4, 37.8, 33.1, 1.9, 15.2, 16.1, 22.0, 26.8,
         7.6, 15.6, 25.3, 32.7, 21.7, 42.8, 15.9, 37.6, 11.0, 23.5, 20.0, 31.5, 10.9, 9.4, 30.4, 33.4, 0.1, 21.9, 28.4,
         31.3, 48.4, 48.1, 16.0, 21.8, 10.4, 22.4, 15.0, 12.8, 36.3, 9.1, 27.7, 9.9, 2.5, 26.0, 49.1, 37.1, 7.3, 11.9,
         12.9, 2.4, 14.6, 22.9, 47.0, 44.2, 12.1, 15.8, 42.2, 20.6, 28.2, 39.5, 42.5, 13.4, 10.8, 25.1, 13.0, 43.2,
         18.7, 41.5, 42.6, 48.0, 15.1, 40.8, 14.1, 0.4, 47.5, 24.3, 22.5, 28.1, 49.0, 42.7, 40.4, 1.3, 25.8, 26.9, 24.1,
         14.7, 11.6, 27.2, 15.5, 29.5, 6.6, 12.3, 47.3, 24.2, 19.6, 9.8, 5.6, 5.1, 23.7, 49.8, 17.9, 30.0, 14.3, 5.8,
         0.9, 42.1, 25.6, 46.1, 5.2, 22.2, 46.8, 15.4, 33.9, 30.9, 5.5, 46.5, 21.1, 42.9, 5.7, 27.9, 38.3, 11.5, 28.7,
         2.3, 4.9, 26.6, 17.7, 42.4, 32.3, 20.4, 3.1, 25.0, 41.6, 8.3, 1.1, 41.1, 7.9, 48.9, 28.3, 38.4, 32.6, 39.0,
         29.3, 4.7, 23.2, 11.8, 35.0, 2.6, 13.1, 19.3, 10.6, 9.7, 43.9, 46.4, 34.2, 28.8, 16.3, 7.5, 40.9, 33.3, 0.5,
         13.2, 29.6, 20.3, 13.6, 19.4, 21.6, 21.5, 0.3, 10.7, 5.4, 29.8, 45.9, 23.9, 36.9, 29.4, 4.8, 46.3, 3.0, 8.2,
         42.3, 37.2, 33.8, 33.7, 41.8, 38.9, 11.2, 31.9, 44.8, 38.2, 12.6, 45.2, 12.4, 20.9, 27.8, 2.8, 35.1, 49.4,
         36.4, 24.7, 0.7, 22.7, 34.8, 34.1, 33.2, 35.5, 35.9, 11.7, 24.6, 35.2, 12.0, 22.1, 42.0, 28.6, 6.8, 32.0, 24.4,
         49.7, 11.4, 37.3, 38.5, 35.4, 45.3, 30.3, 40.1, 33.6, 44.6, 33.5, 20.8, 44.7, 39.2, 10.5, 21.4, 43.0, 10.2,
         8.5, 49.6, 13.7, 24.8, 13.3, 8.6, 12.2, 16.8, 40.0, 12.5, 6.9, 14.9, 38.6, 35.6, 14.8, 31.4, 20.2, 47.6, 34.7,
         26.4, 32.5, 19.2, 43.4, 17.1, 31.7, 21.0, 6.2, 25.5, 6.5, 22.8, 27.5, 4.1, 44.9, 25.2, 28.5, 34.6, 48.7, 23.3,
         23.1, 32.1, 30.2, 43.1, 44.0, 26.2, 11.1, 49.5, 46.9, 16.4, 30.5, 41.9, 46.7, 30.8, 31.2, 8.1, 1.4, 34.9, 14.5,
         26.3, 17.0, 46.2, 9.6, 7.2, 18.8, 29.0]

print('Исходный массив:', array)
print('Отсортированный массив:', merge_sort(array))

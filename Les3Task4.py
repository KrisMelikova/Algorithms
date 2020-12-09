# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 100
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

my_dict = {}
how_many = 0
i = 0

for x in array:
    my_dict[x] = my_dict[x] + 1 if x in my_dict else 1
    if my_dict[x] > how_many:
        how_many, i = my_dict[x], x
print(f'Число {i} встречается {how_many} раз')

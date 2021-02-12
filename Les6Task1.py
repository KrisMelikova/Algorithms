# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

# Описанный ниже код для посчета памяти, выделенной под переменные, актуален для выбранной задачи. В самом конце ПЗ
# описала более универсальный вариант, который может подсчитывать и содержимое (списка, например). Так как в каждом
# варианте кода есть locals(), вариации нужно запускать отдельно.


# Python 3.8.5 / OS Type: 64-bit

import sys
from gc import get_referents

# вариант 1

a = int(input('Введите целое трехзначное число'))

sum = (a // 100) + ((a % 100) // 10) + (a % 10)
mult = (a // 100) * ((a % 100) // 10) * (a % 10)


print(f'Сумма цифр введенного числа = {sum}')
print(f'Произведение цифр введенного числа = {mult}')

my_dict = locals().copy()
size = 0

for key, item in my_dict.items():
    if key.startswith('_'):
        continue
    if isinstance(item, (str, int)):
        size += sys.getsizeof(item)

print(f'Памяти выделено под переменные: {size} байт') # Памяти выделено под переменные: 84 байт

# вариант 2

a = input('Введите целое трехзначное число')

sum = 0
mult = 1

for i in a:
    sum = sum + int(i)
    mult = mult * int(i)
print(f'Сумма цифр введенного числа: {sum}')
print(f'Произведение цифр введенного числа: {mult}')

my_dict = locals().copy()
size = 0

for key, item in my_dict.items():
    if key.startswith('_'):
        continue
    if isinstance(item, (str, int)):
        size += sys.getsizeof(item)

print(f'Памяти выделено под переменные: {size} байт') # Памяти выделено под переменные: 158 байт

# вариант 3

a = int(input('Введите целое трехзначное число'))

x = a // 100
y = a % 100 // 10
z = a % 10

sum = x + y + z
mult = x * y * z

print(f'Сумма цифр введенного числа: {sum}')
print(f'Произведение цифр введенного числа: {mult}')

y_dict = locals().copy()
size = 0

for key, item in my_dict.items():
    if key.startswith('_'):
        continue
    if isinstance(item, (str, int)):
        size += sys.getsizeof(item)

print(f'Памяти выделено под переменные: {size} байт') # Памяти выделено под переменные: 168 байт

# Исходя из полученных мной вариантов с точки зрения оценки памяти наиболее оптимален первый вариант задачи, где
# для переменных выделено 84 байта.

# Более универсальный вариант:
'''
my_dict = locals().copy()
size = 0
ids = set()

for key, item in my_dict.items():
    if key.startswith('_'):
        continue
    if isinstance(item, (str, int, list)):
        objects = [item]
        while objects:
            ref = []
            for item in objects:
                if id(item) not in ids:
                    ids.add(id(item))
                    size += sys.getsizeof(item)
                    ref.append(item)
            objects = get_referents(*ref)

print(f'Памяти выделено под переменные: {size} байт')
'''
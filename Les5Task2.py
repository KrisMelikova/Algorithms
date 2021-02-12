# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как коллекция,
# элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F.
# Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

numbers = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
print(numbers)

first = list(input('Введите первое число в шестнадцатеричной системе счисления'))
second = list(input('Введите второе число в шестнадцатеричной системе счисления'))

print(first)
print(second)

if len(first) > len(second):
    first, second = second, first

second = second[::-1]

res = deque([])
k = 0
n = -1
c = 0

for i in second:
    a = numbers.index(i)
    b = numbers.index(first[n])
    c = (a + b + k) % 16
    res.appendleft(numbers[c])

    if (a + b) > 15:
        k = 1
    else:
        k = 0

    n -= 1

    if n == - len(first) - 1:
        break

difference = len(second) - len(first)

if difference:
    for i in second[-difference:]:
        c = numbers[(numbers.index(second[-difference]) + k) % 16]
        res.appendleft(c)
        if numbers.index(second[-difference]) + k > 15:
            k = 1
        else:
            k = 0
    if k == 1:
        res.appendleft('1')

print(f'Итог сложения: {res}')
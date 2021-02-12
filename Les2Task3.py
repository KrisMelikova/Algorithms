#Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
#https://drive.google.com/file/d/1yeYoVOXCuh0wwiB_LmTJsX0Kdq4y0iLG/view?usp=sharing

a = 1
max_sum = 0
max_num = 0

def rec_func(a):
    if a < 10:
        return a
    else:
        return a % 10 + rec_func(a // 10)

while a != 0:
    a = int(input('Введите натуральное число'))

    d = rec_func(a)

    if d > max_sum:
        max_sum = d
        max_num = a

print(f'Наибольшая сумма цифр: {max_sum} у числа: {max_num}')











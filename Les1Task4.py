#Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
# https://drive.google.com/file/d/1WXaZG1oh7tEwHe_1qV5Ml0TC2qCV-A0J/view?usp=sharing

a = int(input('Введите первое число'))
b = int(input('Введите второе число'))
c = int(input('Введите третье число'))

if c > a > b:
    print(f'Среднее число: {a}')
elif a > c > b:
    print(f'Среднее число: {c}')
else:
    print(f'Среднее число: {b}')


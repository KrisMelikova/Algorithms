# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
#https://drive.google.com/file/d/1yeYoVOXCuh0wwiB_LmTJsX0Kdq4y0iLG/view?usp=sharing

n = 1
a = int(input('Введите число'))

def el_sum(n, a):
    if a == 1:
        return n
    else:
        return n + el_sum(n / -2, a - 1)

b = el_sum(n, a)
print(b)








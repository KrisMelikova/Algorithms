#Посчитать четные и нечетные цифры введенного натурального числа.
#Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)
#https://drive.google.com/file/d/1yeYoVOXCuh0wwiB_LmTJsX0Kdq4y0iLG/view?usp=sharing

odd = 0 # нечетное число
even = 0 # четное число

a = int(input('Введите натуральное число'))

while a != 0:
    b = a % 10
    if b % 2 == 0:
        even += 1
    else:
        odd += 1
    a = a // 10

print(f'Нечетных цифр в числе: {odd}, четных цифр в числе:{even}')
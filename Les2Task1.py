# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.
#https://drive.google.com/file/d/1yeYoVOXCuh0wwiB_LmTJsX0Kdq4y0iLG/view?usp=sharing

user_number = input("Введите целое число, состоящее минимум из двух цифр")

for i in reversed(user_number):
    print(i, end = '')

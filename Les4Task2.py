# Нахождение i-го по счёту простого числа.
# вариант решения задачи без использования «Решета Эратосфена»
num = int(input('Введите число'))

new_list = [2]
i = 2

while True:
    i += 1
    n = 2
    while True:
        if i % n == 0:
            break
        else:
            n += 1
            if n == i:
                new_list.append(i)
                break
    if len(new_list) == num:
        print(f'{num}-е простое число в списке: {i}')
        break

print(f'Список простых чисел: {new_list}')

# вариант решения задачи с использованием «Решета Эратосфена»

num = int(input('Введите число'))

num_2 = num * num
my_list = [i for i in range(num_2)]
my_list[1] = 0

for i in range(2, num_2):
    if my_list[i] != 0:
        a = i * 2
        while a < num_2:
            my_list[a] = 0
            a += i
new_my_list = [i for i in my_list if i != 0]

for i, item in enumerate(new_my_list):
     if i >= num - 1:
         break
print(f'{num}-е по счету простое число: {new_my_list[i]}')
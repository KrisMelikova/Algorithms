#В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

my_list = []
my_diap = []

for i in range(2, 100):
    my_list.append(i)

for m in range(2, 10):
    my_diap.append(m)

for elem in my_diap:
    a = [] #создаю пустой список, чтобы потом подсчитать количество его элементов
    for cell in my_list:
        if cell % elem == 0:
           a.append(cell)
    print(f'Количество чисел кратных {elem}: {len(a)} ')

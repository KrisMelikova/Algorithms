# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

SIZE_M = 4
SIZE_N = 5

matrix = [[0 for _ in range(SIZE_M)] for _ in range(SIZE_N)]
print(matrix)

for line in matrix:
    for i in range(len(line) - 1):
        line[i] = int(input('Введите число'))

for line in matrix:
    for i, item in enumerate(line):
        line[3] = line[0] + line[1] + line[2]
        print(f'{item:>5}', end='')
    print('')






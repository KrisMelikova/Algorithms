#Задание 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import OrderedDict

num = int(input('Сколько будет компаний?'))
my_dict = {}
i = 1
sum_profit_all = 0
comp_avrg_all = 0

while i <= num:
    user_comp = input("Введите название компании")
    user_first = int(input("Введите прибыль за первый квартал в рублях"))
    user_second = int(input("Введите прибыль за второй квартал в рублях"))
    user_third = int(input("Введите прибыль за третий квартал в рублях"))
    user_fourth = int(input("Введите прибыль за четвертый квартал в рублях"))

    sum_profit = user_first + user_second + user_third + user_fourth
    sum_profit_all += sum_profit
    comp_avrg_all = sum_profit_all / num

    my_dict[user_comp] = sum_profit
    my_odict = OrderedDict(sorted(my_dict.items()))

    i += 1

print(f'Средняя прибыль за год для всех предприятий:{comp_avrg_all:.2f} руб.')

for key in my_odict:
    if my_odict[key] > comp_avrg_all:
        print(f'Прибыль выше среднего: {key}')
    elif my_odict[key] < comp_avrg_all:
        print(f'Прибыль ниже среднего: {key}')
    else:
        print(f'У этого предприятия прибыль равна средней прибыли за год для всех предприятий: {key}')

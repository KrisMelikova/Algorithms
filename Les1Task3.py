#Определить, является ли год, который ввел пользователь, високосным или не високосным.
#https://drive.google.com/file/d/1WXaZG1oh7tEwHe_1qV5Ml0TC2qCV-A0J/view?usp=sharing

b = 'не високосный год'
c = 'високосный'

a = int(input('Введите год, чтобы узнать високосный он или нет'))

if a % 4 == 0:
    if a % 100 == 0:
        if a % 400 == 0:
            print(f'{c}')
        else:
            print(f'{b}')
    else:
        print(f'{c}')
else:
    print(f'{b}')

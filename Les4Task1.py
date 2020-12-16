# Посчитать четные и нечетные цифры случайно сгенерированного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)

import random
import timeit
import time
import cProfile

# первый вариант решения задачи

def func(n, m):
    odd = 0  # нечетное число
    even = 0  # четное число

    a = random.randint(n, m)

    while a != 0:
        b = a % 10
        if b % 2 == 0:
            even += 1
        else:
            odd += 1
        a = a // 10

print(timeit.timeit('func(10**2,10**3)', number = 1000, globals = globals())) # 0.002554295992013067
print(timeit.timeit('func(10**5,10**6)', number = 1000, globals = globals())) # 0.003272076020948589
print(timeit.timeit('func(10**10,10**11)', number = 1000, globals = globals())) # 0.0046668159775435925

# В алгоритме использован один цикл, его  сложность  - линейная, т.е. О(n), что видно и на замерах.

cProfile.run('func(10**2,10**3)')
cProfile.run('func(10**5,10**6)')
cProfile.run('func(10**10,10**11)')

'''
все три прогона cProfile:

         9 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 Les4Task1.py:12(func)
        1    0.000    0.000    0.000    0.000 random.py:200(randrange)
        1    0.000    0.000    0.000    0.000 random.py:244(randint)
        1    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
'''
# второй вариант решения задачи


def func_2(n, m):
    odd, even = 0, 0

    a = str(random.randint(n, m))

    for elem in a:
        if elem in ['1', '3', '5', '7', '9']:
            odd += 1
        else:
            even += 1


print(timeit.timeit('func_2(10**2,10**3)', number = 1000, globals = globals())) # 0.0017295759753324091
print(timeit.timeit('func_2(10**5,10**6)', number = 1000, globals = globals())) # 0.002057329984381795
print(timeit.timeit('func_2(10**10,10**11)', number = 1000, globals = globals())) # 0.002971656038425863

# В алгоритме использован один цикл, также линейная сложность  - О(n), подтвержденная проверкой timeit.


cProfile.run('func_2(10**2,10**3)')
cProfile.run('func_2(10**5,10**6)')
cProfile.run('func_2(10**10,10**11)')

'''
три прогона:
        9 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 Les4Task1.py:39(func_2)
        1    0.000    0.000    0.000    0.000 random.py:200(randrange)
        1    0.000    0.000    0.000    0.000 random.py:244(randint)
        1    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


         9 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 Les4Task1.py:39(func_2)
        1    0.000    0.000    0.000    0.000 random.py:200(randrange)
        1    0.000    0.000    0.000    0.000 random.py:244(randint)
        1    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


         10 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 Les4Task1.py:39(func_2)
        1    0.000    0.000    0.000    0.000 random.py:200(randrange)
        1    0.000    0.000    0.000    0.000 random.py:244(randint)
        1    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        2    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


'''

# третий вариант решения задачи (изощренный)
# его пришлось несколько модифицировать, чтобы хоть что-то увидеть

def func_3(n, m):
    odd = []
    even = []

    a = str(random.randint(n, m))

    for i in range(len(a)):
        _ = a[i]
        for n in range(len(a)):
            _ = a[n]
            if i == n:
                elem = int(a[n])
            time.sleep(0.0001)
        if elem % 2 == 0:
            odd.append(elem)
        else:
            even.append(elem)

print(timeit.timeit('func_3(10**2,10**3)', number = 1000, globals = globals())) # 1.5928635110030882
print(timeit.timeit('func_3(10**5,10**6)', number = 1000, globals = globals())) # 6.354263807006646
print(timeit.timeit('func_3(10**10,10**11)', number = 1000, globals = globals())) # 21.307233610015828

# У алгоритма есть цикл, вдложенный в другой цикл, его сложность  - квадратичная, т.е. О(n**2). Подтверждено замерами.

cProfile.run('func_3(10**2,10**3)')
cProfile.run('func_3(10**5,10**6)')
cProfile.run('func_3(10**10,10**11)')

'''
три прогона:
25 function calls in 0.002 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.002    0.002 <string>:1(<module>)
        1    0.000    0.000    0.002    0.002 Les4Task1.py:64(func_3)
        1    0.000    0.000    0.000    0.000 random.py:200(randrange)
        1    0.000    0.000    0.000    0.000 random.py:244(randint)
        1    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
        4    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        9    0.002    0.000    0.002    0.000 {built-in method time.sleep}
        3    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


         58 function calls in 0.006 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.006    0.006 <string>:1(<module>)
        1    0.000    0.000    0.006    0.006 Les4Task1.py:64(func_3)
        1    0.000    0.000    0.000    0.000 random.py:200(randrange)
        1    0.000    0.000    0.000    0.000 random.py:244(randint)
        1    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
        7    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       36    0.006    0.000    0.006    0.000 {built-in method time.sleep}
        6    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


         153 function calls in 0.020 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.020    0.020 <string>:1(<module>)
        1    0.000    0.000    0.020    0.020 Les4Task1.py:64(func_3)
        1    0.000    0.000    0.000    0.000 random.py:200(randrange)
        1    0.000    0.000    0.000    0.000 random.py:244(randint)
        1    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.020    0.020 {built-in method builtins.exec}
       12    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      121    0.020    0.000    0.020    0.000 {built-in method time.sleep}
       11    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

'''

# Первый и второй варианты решения задачи примерно одинаковы в плане оптимальности, т.к. "while" и "for in" практически идентичны.
# Третий вариант искусственно усложнен. Безусловно, он не оптимален, но на нем можно увидеть уже хоть какие-то отличия в производительности,
# особенно если запускать в терминале команду python3 -m cProfile (имя_файла).py.
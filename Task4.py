# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов
# (значения от -100 до 100) многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте
# 0 просто пропускаем данную итерацию степени
# Записываем результат в файл.

# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0

import random

k = int(input("Введите натуральную степень k = "))

lst = []

for i in range(k):
    lst.append(random.randint(-100, 100))

coef = ''
if len(lst) < 1:
    coef = 'x = 0'
else:
    for i in range(len(lst)):
        if i != len(lst) - 1 and  i != len(lst) - 2 and  lst[i] != 0:
            coef += f'{lst[i]}x^{len(lst)-i-1}'
            if lst[i+1] != 0:
                coef += ' + '
        elif i == len(lst) - 2 and lst[i] != 0:
            coef += f'{lst[i]}x'
            if lst[i+1] != 0:
                coef += ' + '
        elif i == len(lst) - 1 and lst[i] != 0:
            coef += f'{lst[i]} = 0'
        elif i == len(lst) - 1 and lst[i] == 0:
            coef += ' = 0'

with open('file.txt', 'w') as data:
    data.write(coef)

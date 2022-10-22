# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x + 33 = 0

# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x + 53 = 0


import random


def create_file(file,mode):
    with open(file, 'w') as data:
        data.write(mode)


def ran():
    return random.randint(-100,100)


def assing_coef(k):
    lst = [ran() for i in range(k+1)]
    return lst
    

def convert_poly(k):
    lst= k[::-1]
    coef = ''
    if len(lst) < 1:
        coef = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                coef += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    coef += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                coef += f'{lst[i]}x'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    coef += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                coef += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                coef += ' = 0'
    return coef


def degree_poly(k):
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i+1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num


def k_mn(k):
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num


def parsing_poly(st_):
    st_ = st_[0].replace(' ', '').split('=')
    st_ = st_[0].split('+')
    lst = []
    l = len(st_)
    k = 0
    if degree_poly(st_[-1]) == -1:
        lst.append(int(st_[-1]))
        l -= 1
        k = 1
    i = 1 
    i_i = l-1 
    while i_i >= 0:
        if degree_poly(st_[i_i]) != -1 and degree_poly(st_[i_i]) == i:
            lst.append(k_mn(st_[i_i]))
            i_i -= 1
            i += 1
        else:
            lst.append(0)
            i += 1
        
    return lst
    

k1 = int(input("Введите натуральную степень для первого файла k = "))
k2 = int(input("Введите натуральную степень для второго файла k = "))
coef1 = assing_coef(k1)
coef2 = assing_coef(k2)
create_file("file1_1.txt", convert_poly(coef1))
create_file("file1_2.txt", convert_poly(coef2))



with open('file1_1.txt', 'r') as data:
    st1 = data.readlines()
with open('file1_2.txt', 'r') as data:
    st2 = data.readlines()

print(f"1-й → {st1}")
print(f"2-й → {st2}")

lst1 = parsing_poly(st1)
lst2 = parsing_poly(st2)

l = len(lst1)

if len(lst1) > len(lst2):
    l = len(lst2)
lst_new = [lst1[i] + lst2[i] for i in range(l)]

if len(lst1) > len(lst2):
    mm = len(lst1)
    for i in range(l,mm):
        lst_new.append(lst1[i])
else:
    mm = len(lst2)
    for i in range(l,mm):
        lst_new.append(lst2[i])

create_file("file1_res.txt", convert_poly(lst_new))

with open('file1_res.txt', 'r') as data:
    st3 = data.readlines()
print(f"Сложение → {st3}")




























# Задайте последовательность цифр. 
# Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

numbers = list(input('Задайте последовательность цифр: '))
list_ = []
new_list = []

for i in numbers:
    i = int(i)
    list_.append(i)     
print(list_)

compare = list_[0]

for j in list_:
    if j != compare:
        new_list.append(j)
    else:
        compare = j
print(new_list)

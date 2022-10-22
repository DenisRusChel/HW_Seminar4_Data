# Задайте последовательность цифр. 
# Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

numbers = list(input('Задайте последовательность цифр: '))

list_ = []

for i in numbers:
    i = int(i)
    list_.append(i)     


list_replay = []

for i in list_:
    replay = 0
    for j in list_:
        if j == i:
            replay +=1
    list_replay.append(replay)
    

single_item = []

for i in range(len(list_replay)):
    if list_replay[i] == 1:
        single_item.append(list_[i])

print(f'{list_} → {single_item}')


# Вычислить число Пи c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001


k = 1
sum = 0
for i in range(5000000):
    if i % 2 == 0:
        sum += 4/k
    else:
        sum -= 4/k
    k += 2
print(sum)

d = input('Введите точность d: ')
length_d = abs(d.find('.') - len(d)) - 1
print(f'при d = {d}, π = {str(sum)[:length_d+2]}')




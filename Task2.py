# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

num = int(input('Введите число: '))

list_simple = []
digit = 2

while num > 1:
    if num % digit == 0:
        list_simple.append(digit)
        num = num // digit
    else:
        digit = digit + 1
print(list_simple)




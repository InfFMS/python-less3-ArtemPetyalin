# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить минимальное и максимальное из введённых чисел.
a = int(input())
max = a
min = a
while a != 0:
    if a > max:
        max = a
    elif a < min:
        min = a
    a = int(input())
if min != 0 and max != 0:
    print('Минимальное число: ' + str(min))
    print('Максимальное число: ' + str(max))
else:
    print('Нет чисел для анализа.')
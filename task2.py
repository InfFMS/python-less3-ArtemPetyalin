# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, сколько было введено двузначных натуральных чисел,
# и сколько других.
a = int(input())
n = 0
other = 0
while a != 0:
    if a >= 10 and a < 100:
        n += 1
    else:
        other += 1
    a = int(input())
print ('Двузначных чисел: ' + str(n) + ' и ' + 'Других чисел: ' + str(other))

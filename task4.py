# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить сумму тех введённых чисел, которые делятся на 5.
a = int(input())
sum = 0
while a != 0:
    if a % 5 == 0:
        sum += a
    a = int(input())

print('Сумма чисел, делящихся на 5: ' + str(sum))
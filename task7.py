# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить минимальное из введённых чисел Фибоначчи.
# Вывести "нет", если чисел Фибоначчи в последовательности нет.
# Числа Фибоначчи – это последовательность чисел,
# которая начинается с двух единиц и каждое следующее число
# равно сумме двух предыдущих: 1, 1, 2, 3, 5, 8, 13, …
a = 1
b = 1
c = int(input())
fi_list = []

while c != 0:

    if c == 1:
        fi_list.append(c)

    while c >= a + b:

        if c == a + b:
            fi_list.append(c)
            c -= 1

        elif a > b:
            b += a

        elif b >= a:
            a += b


    c = int(input())
    a = 1
    b = 1


if len(fi_list) == 0:
    print('нет')

else:
    answer = fi_list[0]

    for i in range (len(fi_list) - 1):

        if fi_list[i] < answer:
            answer = fi_list[i]

    print('Минимальное число Фибоначчи: ' + str(answer))
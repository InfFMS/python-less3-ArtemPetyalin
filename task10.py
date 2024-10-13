# с клавиатуры вводится число N, а затем – N натуральных чисел.
# Определить минимальное и максимальное среди простых чисел
# (которые делятся на сами не себя и на 1).
# Если таких чисел не было, вывести "нет".

N = int(input())
num_list = []

for i in range(N):
    a = int(input())
    divr = 1
    divr_amnt = 0

    while divr <= a:

        if a % divr == 0:
            divr_amnt += 1

        divr += 1

    if divr_amnt == 2:
        num_list.append(a)

if len(num_list) > 0:
    max = num_list[0]
    min = num_list[0]

    for i in range(len(num_list)):

        if num_list[i] > max:
            max = num_list[i]

        elif num_list[i] < min:
            min = num_list[i]

    print('Минимальное простое число: ' + str(min))
    print('Максимальное простое число: ' + str(max))

else:
    print('нет')
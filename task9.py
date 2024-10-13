# с клавиатуры вводится число N, а затем – N целых чисел.
# Определить минимальное и максимальное среди двузначных чисел,
# которые делятся на 3. Если таких чисел не было, вывести "нет".

N = int(input())
num_list = []

if N > 0:

    for i in range(N):
        a = int(input())

        if abs(a) > 9 and abs(a) < 100 and a % 3 == 0:
            num_list.append(a)


if len(num_list) == 0:
    print('нет')

else:
    min, max = num_list[0], num_list[0]
    for i in range(len(num_list)):

        if num_list[i] < min:
            min = num_list[i]

        elif num_list[i] > max:
            max = num_list[i]

print('Минимальное двузначное число, делящееся на 3: ' + str(min))
print('Максимальное двузначное число, делящееся на 3: ' + str(max))

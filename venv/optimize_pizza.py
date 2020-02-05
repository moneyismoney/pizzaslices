#!/bin/python3

import os
import sys
import time


def iterate_till_win(_list_of_pizzas, _slices_maximum):
    if _slices_maximum < 0:
        return 0


def delta(_list_of_pizzas, _slices_maximum):
    return _list_of_pizzas.count() - _slices_maximum


print('Script works!')
print(os.environ['HOME'])

# input_filename = 'c_medium.in';
input_filename = 'e_also_big.in';

fptr = open(os.environ['HOME'] + '/' + input_filename, 'r')

# 1.[Dmytro] Вичитати вхідний файл
# Вхідний параметр: файл на диску з назвою b_small.in
# Вихідний параметр1: Масив(список чи кортеж) input_data[], де перший елемент - перший рядок, другий елемент - другий рядок тощо
# на майбутнє переробити на numpy
start_time = time.time()
with open(input_filename) as f:
    slices, pizza = f.readline().split()
    input_data = f.readline()
    input_data = list(map(int, input_data.split()))
    print(slices, pizza, input_data)


    # for i, line in enumerate(f):
    #     if i == 0:
    #         slices_maximum = int(line.split()[0])
    #         number_of_lines = int(line.split()[1])
    #     else:
    #         slice_of_type = list(int(number_of_slices) for number_of_slices in line.split())
    #
    # print(slices_maximum, number_of_lines, slice_of_type)

print("--- %s seconds ---" % (time.time() - start_time))
# 2. Зробити цикл, який проходить по всім елементам input_data[]

# 3. В циклі
#   3.1. Якщо це перший рядок зберегти в змінну slices_maximum перше число, в number_of_lines друге число
#   3.2. Якщо це наступні рядки: В новий список(кортеж) slice_of_type[] розпарсити string так, щоб його індекс відповідав порядковому номеру,
#   а значення - цифровому значенню

# 4.(Найважче)
#   4.1 Написати функцію (def iterate_till_win()), яка буде по одному виключати елементи зі списку і ітераційно порівнюватиме суму значень
#       з slices_maximum. Важливо: міряти серверний час
#   4.2 Допоміжна функція рахує суму всіх елементів(def delta()) і віднімає slices_maximum

# while True:
    # if sum(input_data) <= slices:
    #     break
    # input_data.pop(-1)

# 5.[Oleh] Згенерувати файл результату
# fptr = open(os.environ['HOME'], 'w')

# fptr.write(str(result) + '\n')

# fptr.close()





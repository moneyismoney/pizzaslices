#!/bin/python3

import os
import sys
import time


# input_filename = 'e_also_big.in'
input_filename = 'base.in'

start_time = time.time()

# 1.[Dmytro] Вичитати вхідний файл
# Вхідний параметр: файл на диску з назвою b_small.in
# Вихідний параметр1: Масив(список чи кортеж) input_data[], де перший елемент - перший рядок, другий елемент - другий рядок тощо
# на майбутнє переробити на numpy
# 2. Зробити цикл, який проходить по всім елементам input_data[]
# 3. В циклі
#   3.1. Якщо це перший рядок зберегти в змінну slices_maximum перше число, в number_of_lines друге число
#   3.2. Якщо це наступні рядки: В новий список(кортеж) slice_of_type[] розпарсити string так, щоб його індекс відповідав порядковому номеру,
#   а значення - цифровому значенню

with open('data/' + input_filename) as f:
    slices, pizza = map(int, f.readline().split())
    input_data = list(map(int, f.readline().split()))

    sum_input_data = sum(input_data)

# 4.(Найважче)
#   4.1 Написати функцію (def iterate_till_win()), яка буде по одному виключати елементи зі списку і ітераційно порівнюватиме суму значень
#       з slices_maximum. Важливо: міряти серверний час
#   4.2 Допоміжна функція рахує суму всіх елементів(def delta()) і віднімає slices_maximum

while True:
    if sum_input_data <= slices:
        break
    sum_input_data -= input_data.pop()

# 5.[Oleh] Згенерувати файл результату
## На виході очіують не самі числа, а їх індекси
final_output = []
for current_index in range(0, len(input_data)):
    final_output.append(current_index)
input_data = final_output
##
input_data = list(map(str, input_data))

with open('result/' + input_filename, 'w') as f:
    f.write(f"{len(input_data)}")
    f.write(f"\n{' '.join(input_data)}")

print("--- %s seconds ---" % (time.time() - start_time))

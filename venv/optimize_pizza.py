#!/bin/python3

import os
import sys

print('Script works!')
print(os.environ['HOME'])

input_filename = 'c_medium.in';

fptr = open(os.environ['HOME']+'/'+input_filename, 'r')

for line in fptr:
    print(line)
    print('\n')



# 1. Вичитати вхідний файл
# Вхідний параметр: файл на диску з назвою b_small.in
# Вихідний параметр1: Масив(список чи кортеж) input_data[], де перший елемент - перший рядок, другий елемент - другий рядок тощо


# 2. Зробити цикл, який проходить по всім елементам input_data[]

# 3. В циклі
#   3.1. Якщо це перший рядок зберегти в змінну slices_maximum перше число, в number_of_lines друге число
#   3.2. Якщо це наступні рядки: В новий список(кортеж) slice_of_type[] розпарсити string так, щоб його індекс відповідав порядковому номеру,
#   а значення - цифровому значенню

# 4.(Найважче)
#   4.1 Написати функцію (def iterate_till_win()), яка буде по одному виключати елементи зі списку і ітераційно порівнюватиме суму значень
#       з slices_maximum. Важливо: міряти серверний час
#   4.2 Допоміжна функція рахує суму всіх елементів(def delta()) і віднімає slices_maximum



# 5. Згенерувати файл результату
#fptr = open(os.environ['HOME'], 'w')

#fptr.write(str(result) + '\n')

#fptr.close()
#!/bin/python3

import os
import sys

#
# Complete the handshake function below.
#
def handshake(n):
    return  1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = handshake(n)

        fptr.write(str(result) + '\n')

    fptr.close()

# 1. Вичитати вхідний файл
# Вхідний параметр: файл на диску з назвою b_small.in
# Вихідний параметр1: Масив input_data[]


# 2. Зробити цикл, який проходить по всім елементам input_data[]

# 3. В циклі
#   3.1. Якщо це перший рядок зберегти в змінну slices_maximum перше число, в number_of_lines друге число
#   3.2. В новий масив зберегти рядки завдань
# 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
# *Пример:*
#
# - 6782 -> 23
# - 0,56 -> 11

# numbers = input('Введите числа: ')
# sum = 0
# for i in numbers:
#     if i != ',':
#         sum += int(i)
# print(sum)


# 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input('input N: '))
# factorial = 1
# for i in range(1, n+1):
#     factorial *= i
#     print(factorial, end=' ')

# 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму, округлённую до трёх
# знаков после точки.
#
# *Пример:*
# - Для n = 6 -> 14.072

# n = int(input('Введите число: '))
#
#
# def sequence(n):
#     return [round((1 + 1 / x) ** x, 2) for x in range(1, n + 1)]
#
# print(sequence(n))
# print(round(sum(sequence(n)), 3))




# 5 Реализуйте алгоритм перемешивания списка.

# list = ['Москва', 4.45, 350, True]
# print(list)
# import random
# random.shuffle(list)
# print('->', list)
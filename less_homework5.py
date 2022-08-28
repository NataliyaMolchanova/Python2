# Урок 5. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension


# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# my_text = 'Как была сделана одна из самых узнаваемых и самыхабв дорогих фотографий в мире абв'
#
# def del_some_words(my_text):
#     my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
#     return " ".join(my_text)
#
# my_text = del_some_words(my_text)
# print(my_text)


# 2. Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
#

# from random import randint
#
# def input_dat(name):
#     x = int(input(f"{name}, сколько возьмёте конфет? можно взять 1 — 28 шт.: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите корректное количество: "))
#     return x
#
#
# def p_print(name, k, counter, value):
#     print(f"{name} взял {k}. Теперь у него {counter} конфет. Осталось на столе {value} конфет.")
#
# player1 = input("Введите имя первого игрока: ")
# player2 = input("Введите имя второго игрока: ")
# value = int(input("Введите количество конфет на столе: "))
# flag = randint(0,2) # флаг очередности
# if flag:
#     print(f"Первым ходит {player1}")
# else:
#     print(f"Первым ходит {player2}")
#
# counter1 = 0
# counter2 = 0
#
# while value > 28:
#     if flag:
#         k = input_dat(player1)
#         counter1 += k
#         value -= k
#         flag = False
#         p_print(player1, k, counter1, value)
#     else:
#         k = input_dat(player2)
#         counter2 += k
#         value -= k
#         flag = True
#         p_print(player2, k, counter2, value)
#
# if flag:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")



# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res


s = input("Введите текст для кодировки: ")
print(f"Текст после кодировки: {coding(s)}")
print(f"Текст после дешифровки: {decoding(coding(s))}")
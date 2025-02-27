# Лабораторная работа №2 ИСТбд-12 Ченакин Владислав

#Написать программу, решающую задачу из 1 лабораторной работы (в соответствии со своим вариантом) со следующими изменениями:
#1.	Входной файл является обыкновенным (т.е. нет требования на «бесконечность» файла);
#2.	Распознавание и обработку делать через регулярные выражения;
#3.	В вариантах, где есть параметр (например К), допускается его заменить на любое число(константу);
#4.	Все остальные требования соответствуют варианту задания лабораторной работы №1.


# Вариант 16 (Лабораторная работа №1).
# Четные двоичные числа, не превышающие 819110, в которых встречается не более одной серии из трех подряд идущих нуля.
# Выводит на экран цифры числа, исключая нули. Отдельно выводится прописью номер позиции, с которой начинается эта серия.

import re

# Создание тестового файла
with open("data.txt", "w") as files:
    files.write("1010101 1111111111000 1111111111111 1011 1011000110 1010000100 101100 1011010 10100001010 101010 10101010 1010101 101010 10101 10101010 101010101 1010 11010 10110011000 10101010001 101001010 11111111")

# Словарь для преобразования позиции серии "000" в пропись (если позиция от 1 до 9)
numbers = {
    1 : "один", 2 : "два", 3 : "три",
    4 : "четыре", 5 : "пять", 6 : "шесть",
    7 : "семь", 8 : "восемь", 9 : "девять"
}

# Функция для поблочного чтения файла и обработки чисел
def read_file(filename):
    with open(filename, "r") as file: # Открываем файл в режиме чтения
        chunk = file.read(12) # Считываем файл блоками по 12 символов
        remainder = "" # Переменная для хранения остатка блока
        number = "" # Переменная для хранения текущего числа
        flag = 1 # Обозначение начала нового числа (если чётная, то чтение числа в блоке окончено и остальное идет в остаток)
        while chunk: # Пока есть данные в файле
            for i in chunk: # Проходим по символам текущего блока
                if i == " ": # Если встречаем пробел
                    flag += 1 # Чтение основного числа в блоке окончено
                    if is_valid_number(number) == 1: # Проверяем число на соответствие условиям
                        print(single_000(number)) # Выводим обработанное число
                    number = "" # Очищаем переменные для следующего числа
                    remainder = ""
                else: # Если считан не пробел, продолжаем запись числа
                    number += i;
                if (flag % 2 == 0): # Если чтение основного числа в блоке окончено
                    remainder += i

            chunk = file.read(12) # Читаем следующий блок

        if number and is_valid_number(number) == 1: #  Проверяем последнее считанное число
            print(single_000(number))

# Функция проверки числа на соответствие условиям
def is_valid_number(number):
    # Проверка: в числе может быть не более одной серии из трёх подряд идущих нулей
    # Проверка: число должно содержать только '0' и '1'
    # Проверка: число не должно превышать 8191 (в десятичной системе). 8191 в 2ой = 1111111111111(13 единиц). Условие не прописывается напрямую, т.к есть ограничение в 13 символов, а также в конце должен стоять 0
    # Проверка: число должно быть чётным (оканчиваться на '0')
    if re.fullmatch(r'^(?!.000.*000)([01]{1,13}0)', number):
        return 1

# Функция преобразования числа по заданным правилам
def single_000(number):
    ones_count = len(re.findall(r'1', number))
    if re.findall(r'000', number):
        return "1" * ones_count + " " + numbers[(re.search(r'000', number)).start() + 1]
    else:
        return "1" * ones_count

read_file("data.txt")
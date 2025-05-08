import time
import math
import matplotlib.pyplot as plt
import pandas as pd


# Рекурсивная реализация
def F_rec(n):
    if n == 1:  # F(1) = 1
        return 1
    if n % 2 == 0 and n > 1:  # F(n) = (-1)**n * (F(n–1) /(2n)!), при четных n > 1 
        return (-1) ** n * (F_rec(n - 1) / math.factorial(2 * n))
    else:  # F(n)=n! при нечетных n > 1
        return math.factorial(n)


# Итерационная реализация
def F_iter(n):
    results = {1: 1}  # Словарь результатов, F(1) = 1
    for i in range(2, n + 1):
        if i % 2 == 0 and i > 1:  # F(n) = (-1)**n * (F(n–1) /(2n)!), при четных n > 1
            results[i] = (-1) ** i * (
                        results[i - 1] / math.factorial(2 * i))  # Берем прошлые значения фунцкия из словаря по ключу
        else:  # F(n)=n! при нечетных n > 1
            results[i] = math.factorial(i)
    return results[n]


max_n = 15  # Для демонстрации работы рекурсии
results = []

for n in range(1, max_n + 1):
    # Рекурсивный способ
    startR = time.perf_counter()
    f_rec = F_rec(n)
    endR = (time.perf_counter() - startR) * 1000  # в милисек вместо сек

    # Итерационный способ
    startI = time.perf_counter()
    f_it = F_iter(n)
    endI = (time.perf_counter() - startI) * 1000  # в милисек вместо сек

    results.append({
        'n': n,
        'F_rec': f_rec,
        'F_iter': f_it,
        'Время выполнен. рекурс. функции': endR,
        'Время выполнен. итерат. функции': endI
    })

# Создание таблицы и графика
df = pd.DataFrame(
    results)  # Создает объект DataFrame(двумерная структура данных, представляющая собой таблицу с метками для строк и столбцов) из списка словарей results
print(df.to_string(
    float_format="%.6f"))  # Преобразует DataFrame в строку для вывода в консоль, Форматирует числа с плавающей точкой, оставляя 6 знаков после запятой,

plt.figure(figsize=(10, 6))  # Создает область для графика 10 на 6 дюймов
plt.plot(df['n'], df['Время выполнен. рекурс. функции'], 'rs-', label='Рекурсия') # 'rs-' красный график, квадр. точки, тип линии - сплошная
plt.plot(df['n'], df['Время выполнен. итерат. функции'], 'bs-', label='Итерации') # 'bs-' синий график, квадр. точки, тип линии - сплошная
plt.xlabel('n') # для подписи оси x
plt.ylabel('Время (мс)') # для подписи оси y
plt.title('Сравнение методов вычисления F(n)') #заголовок
plt.legend() # обязательный элемент для графиков с несколькими наборами данных. Функция автоматически собирает все метки, указанные в plot(), и отображает их в виде легенды
plt.grid(True) #сетка
plt.show()
import itertools
import time

N, K = 9, 4  # 9 вагонов, 4 человека

#Функция измеряет время выполнения другой функции (func) и возвращает: Результат выполнения func, Затраченное время в секундах.
def measure_time(func, N, K): #* - функция может принимать произвольное кол-во аргументов. Они будут собраны в кортеж.
    start = time.perf_counter() # Запись начального времени
    result = func(N, K) # Вызов функции
    end_time = time.perf_counter() # Запись конечного времени
    return result, end_time - start

# Алгоритмический способ с вложенными циклами
def algorithmic_method(N, K):
    result = []
    for v1 in range(1, N+1): #каждый цикл отвечает за выбор вагона для одного конкретного человека
        for v2 in range(1, N+1):
            if v2 != v1: #вагоны не должны совпадать
                for v3 in range(1, N+1):
                    if v3 not in {v1, v2}:
                        for v4 in range(1, N+1):
                            if v4 not in {v1, v2, v3}:
                                result.append((v1, v2, v3, v4))
    return result

# Способ с использованием itertools.permutations
def itertools_method(N, K):
    return list(itertools.permutations(range(1, N+1), K)) #Создает последовательность чисел от 1 до N, Генерирует все перестановки из N элементов по K

# Замеряем времени выполнения и фиксируем результат
result_loop, loop_time = measure_time(algorithmic_method, N, K)
result_itertools, itertools_time = measure_time(itertools_method, N, K)

print(f'Алгоритмический метод: {len(result_loop)} вариантов, время: {loop_time:.6f} сек.')
print(f'Метод itertools: {len(result_itertools)} вариантов, время: {itertools_time:.6f} сек.')
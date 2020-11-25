'''
Бинарный поиск - это когда мы с каждым выбором исключаем половину последовательности.
Например надо угадать число от 0 до 100
50 - мало
75 - много
63 - много
57 - точно
Применим, только если список отсортирован!

O ("о-большое" - скорость работы алгоритма) = log(n)    (log - логарифм по основанию 2)
'''
import time
import math

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low < high:
        mid = math.floor((low + high) / 2)
        guess = list[mid]
        if guess < item:
            # искомый элемент где-то справа
            # сдвигаем левую границу
            low = mid + 1
        elif guess > item:
            # искомый элемент где-то слева
            # сдвигаем правую границу
            high = mid - 1
        elif guess == item:
            return mid

    return None

my_list = [i for i in range(1000)]
my_number = 777
start_time = time.time()
index = binary_search(my_list, my_number)
end_time = time.time()

# Два варианта форматирования строк
# 1)
print(f"Search finished in {end_time - start_time:.10f} seconds")
# 2)
print("Search finished in %1.10f seconds" %(end_time - start_time))


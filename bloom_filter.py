'''

Полное объяснение можно найти здесь:
https://www.geeksforgeeks.org/bloom-filters-introduction-and-python-implementation/

Теории очень много, поэтому писать здесь ее не вижу смысла

Если вкратце, то
1) Есть массив из m элементов, строка, k хэш-функий
2) Строка пропускается через каждую функцию, получаются индексы массива.
3) В массиве на этих индексах элементы становятся единицами (просто биты: 0 или 1)
4) При проверка на наличие строки в массиве она снова пропускается через функции и проверяется, есть
ли на полученных местах единицы. Если есть хотя бы один ноль - то строка отсутствует (не была обработана ранее).
Если все единицы - строка ВОЗМОЖНО была обработана ранее.

--Возможно, потому что могут быть коллизии, и ячейки, которые заполняются словом 'car' могли быть ранее заполнены
словом 'fix'. Здесь вводится вероятность негативно позитивного ответа (когда строка не была обработана ранее, а алгоритм
говорит, что была - p)
-- Есть формулы для рассчета p, m, k. Они применены в примере.

'''

import math
# murmurhash
import mmh3
from random import shuffle
from bitarray import bitarray


# Класс реализует фильтр Блума со всеми присущими ему функциями
class BloomFilter(object):
    # items_count - сколько элементов ожидается хранить
    # fp_prob - false positive probability
    def __init__(self, items_count, fp_prob):
        self.fp_prob = fp_prob
        self.items_count = items_count
        # размер массива битов
        self.size = self._get_size(items_count, fp_prob)
        # количество хэш-функций
        self.hash_count = self._get_hash_count(self.size, items_count)
        # массив битов заданного размера
        self.bit_array = bitarray(self.size)
        # инициализация массива нулями
        self.bit_array.setall(0)

    # @classmethod означает, что метод привязан к самому классу, а не к экземпляру класса
    # используется в суперклассе, чтобы показать, как метод должен вести себя в дочерних
    # @staticmethod используется, когда мы хотим вернуть одно и то же значение независимо от дочернего класса

    # возвращает размер массива битов(m)(по формуле)
    @classmethod
    def _get_size(cls, n, p):
        m = -(n * math.log(p)) / (math.log(2) ** 2)
        return int(m)

    # возвращает количество хэш-функций(k) (по формуле)
    @classmethod
    def _get_hash_count(cls, m, n):
        k = (m / n) * math.log(2)
        return int(k)

    # функция добавляет новый элемент в массива
    def add(self, item):
        codes = []
        for i in range(self.hash_count):
            # создание кода для каждого элемента
            # i выполняет роль зерна в mmh3.hash()
            # с разными зернами будут разные коды
            code = mmh3.hash(item, i) % self.size
            codes.append(code)
            # соответствующую ячейку в массиве приравниваем к 1
            self.bit_array[code] = True

    # функция проверяет наличие элемента в фильтре (массиве)
    def check(self, item):
        for i in range(self.hash_count):
            code = mmh3.hash(item, i) % self.size
            if self.bit_array[code] == False:
                # если хотя бы один бит равен 0, значит слово не обрабатывалось
                return False
        return True


# =======================================================================================================================
n = 20
p = 0.05

filter = BloomFilter(n, p)
print(f'Size of the array is {filter.size}')
print(f'False positive probability is {filter.fp_prob}')
print(f'Number of hash functions is {filter.hash_count}\n')

# слова, которые будем добавлять
words_present = ['abound', 'abounds', 'abundance', 'abundant', 'accessable',
                 'bloom', 'blossom', 'bolster', 'bonny', 'bonus', 'bonuses',
                 'coherent', 'cohesive', 'colorful', 'comely', 'comfort',
                 'gems', 'generosity', 'generous', 'generously', 'genial']
# слова, которые НЕ будем добавлять
words_absent = ['bluff', 'cheater', 'hate', 'war', 'humanity',
                'racism', 'hurt', 'nuke', 'gloomy', 'facebook',
                'geeksforgeeks', 'twitter']

# добавление слов
for word in words_present:
    filter.add(word)

# перемешиваем слова
shuffle(words_present)
shuffle(words_absent)

# создание тестовой выборки: 10 реальных слов + все существующие
test_words = words_present[:10] + words_absent
shuffle(test_words)
for word in test_words:
    # сначала проверяет наличие слова в массиве
    if filter.check(word):
        # а затем проверяем, является ли оно одним из несуществующих
        if word in words_present:
            print(f'Word {word} is probably present')
        # если оно есть в несуществующих словах и в массиве - ложное срабатываение
        else:
            print(f'Word {word} is false positive!')
    else:
        print(f'Words {word} is not present')

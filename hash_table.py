'''

Хэш-функция - это функция, которая принимает слово о возвращает уникальное для него число
1) Она последовательна, то есть при первом вызове для "Ваня" она вернет 55, и при сотом
вызове для "Ваня" вернет 55
2) Она возвращает разные числа для разных слов

Хэш-таблица - это совокупность хэш-функции и массива.
Допустим, для "Катя" функция вернула 5 - значит, имя "Катя" поместим в 5 ячейку массива.
При повторном вызове, если нам надо найти в массиве имя "Катя" мы просто передадим его в
хэш-функцию, и она вернет индекс.

В Python роль хэш-таблицы играют словари

Популярным примером работы хэширования является кэширование. Браузер кэширует часто посещаемые страницы, и
когда вы переходите на них в очередной раз - просто загружает их из памяти.
'''

# функция проверяет дубликаты на голосовании
voted = {}

def check_voter(voted, name):
    if voted.get(name):
        print("kick them out!")
    else:
        print("allow them to vote!")
        voted[name] = True

check_voter(voted, 'ivan')
check_voter(voted, 'max')
check_voter(voted, 'adit')
check_voter(voted, 'ivan')
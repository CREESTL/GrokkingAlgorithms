'''

Поиск в ширину позволял найти самых короткий маршрут, где длина определялась только количеством ребер графа.
Если же граф является взвешенным, то нужно применять алгоритм Дийкстры:
1) Пока остаются необработанные узлы:
2) Взять узел, ближайший к началу (необработанный)
3) Обновить длину пути от начала до всех его соседей
4) Обновить родителя всех его соседей
5) Пометить узел, как обработанный

Алгоритм Дийкстры нельзя применять для графов с циклами
Алгоритм Дийкстры нельзя применять для графов с отрицательным весом ребер
Алгоритм Дийкстры можно применять только для направленных ациклических графов

Для реализации понадобится три хэш-таблицы: граф, родители, стоимости

'''

# функция задает соседей узла и длину пути до них
def create_graph():
    graph = {}
    # START
    # каждый узел графа - словарь
    graph['start'] = {}
    # указываем расстояние до всех соседних с началом точек
    graph['start']['a'] = 6
    graph['start']['b'] = 2
    # A
    graph['a'] = {}
    graph['a']['fin'] = 1
    # B
    graph['b'] = {}
    graph['b']['a'] = 3
    graph['b']['fin'] = 5
    # FIN
    graph['fin'] = {}
    return graph


# функция задает длину пути от начала до узла
def create_costs():
    # так можно обозначить бесконечность
    inf = float('inf')
    costs = {}
    # это только для первого узла такая длина путей до a и b
    costs['a'] = 6
    costs['b'] = 2
    costs['fin'] = inf
    return costs


# функция создает таблицу родителей узлов (то есть узлы, из которых мы пришли)
def create_parents():
    parents = {}
    parents['a'] = 'start'
    parents['b'] = 'start'
    parents['fin'] = None
    return parents


# функция находит по таблице ячейку с самым коротким путем к ней
def find_lowest_cost_node(costs, processed):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs.keys():
        # цена перехода в узел от начала
        cost = costs[node]
        # стандартный алгоритм поиска минимума
        if (cost < lowest_cost) and (node not in processed):
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


# функция реализует поиск алгоритмом Дийкстры
def dijkstras_search():
    # создание всех таблиц
    costs = create_costs()
    parents = create_parents()
    graph = create_graph()
    # массив узлов, которые уже были обработаны ранее
    processed = []
    # находится ближайший узел для старта
    node = find_lowest_cost_node(costs, processed)
    # массив, содержащий узлы, создающие кратчайший путь
    way = ['start']
    while node is not None:
        # каждый новый узел добавляется в путь
        way.append(node)
        # все соседние узлы
        neighbors = graph[node]
        node_cost = costs[node]
        for n in neighbors.keys():
            # для каждого соседа пересчитывается длина пути
            neighbor_cost = node_cost + neighbors[n]
            # если он меньше, чем имеющаяся в таблице, то данные обновляются
            if costs[n] > neighbor_cost:
                costs[n] = neighbor_cost
                # каждому соседу в родители добавляется обрабатываемый узел
                parents[n] = node
        # обработанный узел помещается в массив
        processed.append(node)
        # снова ищется ближайший узел
        node = find_lowest_cost_node(costs, processed)
    return way


print(f"Shortest way looks like this: {dijkstras_search()}")


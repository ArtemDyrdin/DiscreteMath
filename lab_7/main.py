from random import uniform, randint
import time


def main():
    start_time = time.time()

    createGraphAndPrintResults(1000)
    time1 = time.time()
    print("Время выполнения для графа 1000: ", time1 - start_time)

    createGraphAndPrintResults(2700)
    time2 = time.time()
    print("Время выполнения для графа 2700: ", time2 - time1)

    createGraphAndPrintResults(7300)
    time3 = time.time()
    print("Время выполнения для графа 7300: ", time3 - time2)

    createGraphAndPrintResults(20000)
    time4 = time.time()
    print("Время выполнения для графа 20000: ", time4 - time3)

    createGraphAndPrintResults(53000)
    time5 = time.time()
    print("Время выполнения для графа 53000: ", time5 - time4)


def createGraphAndPrintResults(graphSize):
    '''Составляем граф и исследуем его'''
    maxDistance = 1000 # макс. вес
    graph = createGraph(graphSize, 10, 100, maxDistance)
    addCompleteGraph(graph, 6, maxDistance)
    ensure_connectivity(graph)

    graphAvarageDegree = getAvarageGraphDegree(graph)
    dijkstraIterations = dijkstraAlgorithm(graph, 0)[1]
    bellmanFordIterations = bellmanFordAlgorithm(graph, 0)[1]

    with open(f"{graphSize}_results.txt", "w+", encoding='utf-8') as file:
        file.write(f"Средняя степень вершин в графе: {graphAvarageDegree}\n")
        file.write(f"Количество итераций для алгоритма Дейкстры: {dijkstraIterations}\n")
        file.write(f"Асимптотическая сложность: {graphSize ** 2}\n\n")

        file.write(f"Количество итераций для алгоритма Беллмана-Форда: {bellmanFordIterations}\n")
        file.write(f"Асимптотическая сложность: {graphSize * graphAvarageDegree}\n\n")


def createGraph(size, expectedDegreeMin, expectedDegreeMax, maxDistance):
    '''Генерирование графа'''
    graph = [[0 for _ in range(size)] for _ in range(size)] # матрица смежностей
    for i in range(size):
        lastIndex = i + 1
        # случайное кол-во ребер на вершину
        nonZeroElementsInRow = int(min(uniform(expectedDegreeMin / 2, expectedDegreeMax / 2), size - i - 1))
        while nonZeroElementsInRow > 0:
            lastIndex = int(uniform(lastIndex + 1, size - nonZeroElementsInRow - 1))
            graph[i][lastIndex] = int(uniform(1, maxDistance))
            graph[lastIndex][i] = graph[i][lastIndex]
            nonZeroElementsInRow -= 1
    #
    for i in range(size - 1):
        graph[i][i + 1] = int(uniform(1, maxDistance))
        graph[i + 1][i] = graph[i][i + 1]
    return graph


def addCompleteGraph(graph, completeGraphSize, maxDistance):
    '''Построение подграфа'''
    positionToAddGraph = int(uniform(0, len(graph) - completeGraphSize)) # случайная вершина для подграфа
    for i in range(positionToAddGraph, positionToAddGraph + completeGraphSize):
        for j in range(positionToAddGraph, positionToAddGraph + completeGraphSize):
            if i != j:
                graph[i][j] = int(uniform(1, maxDistance))
                graph[j][i] = graph[i][j]


def ensure_connectivity(graph):
    '''Обеспечение связности графа'''
    size = len(graph)
    visited = [False] * size
    stack = [0]
    # DFS
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            for neighbor, weight in enumerate(graph[node]):
                if weight > 0 and not visited[neighbor]:
                    stack.append(neighbor)
    if not all(visited):
        for i in range(size):
            if not visited[i]:
                graph[i][randint(0, size - 1)] = int(uniform(1, 100)) # новое ребро
                graph[randint(0, size - 1)][i] = graph[i][randint(0, size - 1)]


def getAvarageGraphDegree(graph):
    '''Средняя степень вершин графа'''
    totalDegree = 0
    size = len(graph)
    for row in graph:
        totalDegree += sum(1 for element in row if element > 0)
    return totalDegree / size


def dijkstraAlgorithm(graph, originNode):
    '''Алгоритм Дейкстры'''
    totalIterationsCount = 0
    size = len(graph)
    result = {originNode: 0} # вершина - мин. растояние
    queue = {i: float('inf') for i in range(size)} # вершина - мин. расстояния
    queue[originNode] = 0

    accessibleNodes = getAccessibleNodes(graph) # вершина - смежные вершины 

    while queue:
        closest = min(queue.items(), key=lambda x: x[1]) # мин. вершина-расстояние
        node, mark = closest[0], closest[1]

        for secondNode in accessibleNodes[node]:
            totalIterationsCount += 1
            if secondNode not in queue: # вершина не в очереди - пропускаем
                continue
            path = graph[node][secondNode]
            queue[secondNode] = min(queue[secondNode], mark + path)

        result[node] = queue[node]
        queue.pop(node)

    return result, totalIterationsCount


def bellmanFordAlgorithm(graph, originNode):
    '''Алгоритм Беллмана-Форда'''
    totalIterationsCount = 0
    size = len(graph)
    result = [float('inf')] * size # вершина - мин. расстояние
    result[originNode] = 0

    accessibleNodes = getAccessibleNodes(graph)  # вершина - смежные вершины

    for _ in range(size - 1):
        for startingNode in range(size):
            for secondNode in accessibleNodes[startingNode]:
                totalIterationsCount += 1
                path = graph[startingNode][secondNode]
                result[secondNode] = min(result[secondNode], result[startingNode] + path)

    return result, totalIterationsCount


def getAccessibleNodes(graph):
    '''Получить список смежных вершин для каждой вершины'''
    accessibleNodes = [[] for _ in range(len(graph))]
    for currentNode in range(len(graph)):
        for secondNode in range(len(graph)):
            if graph[currentNode][secondNode] > 0:
                accessibleNodes[currentNode].append(secondNode)
    return accessibleNodes


if __name__ == "__main__":
    main()

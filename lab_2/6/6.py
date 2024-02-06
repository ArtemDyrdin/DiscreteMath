def showGrid(grid):
    for i in grid:
        for j in i:    
            print(j, end="  ")
        print()
    print(end="\n\n")
        

def pathsCounter_1(a, b):
    print('\nPaths Counter 1', end="\n")
    a += 1
    b += 1

    print('\nСоставляем матрицу прямоугольника:')
    grid = [['.']*b for _ in range(a)]
    showGrid(grid)

    print("\nЗаполняем значением '1' точки левого столбца и нижней строки:")
    for i in grid:
        i[0] = 1
    for j in range(b):
        grid[a-1][j] = 1
    showGrid(grid)

    print('\nЗаполняем остальные точки как сумму левой и нижней точки:')
    for i in range(a - 2, -1, -1):
        for j in range(1, b):
            grid[i][j] = grid[i][j - 1] + grid[i + 1][j]
    showGrid(grid)

    print(f'Количество путей: {grid[0][b - 1]}', end="\n\n")

def pathsCounter_2(a, b):
    print('\nPaths Counter 2', end="\n\n")
    a += 1
    b += 1

    print('Составляем матрицу прямоугольника:')
    grid = [['.']*b for _ in range(a)]
    showGrid(grid)

    print("Заполняем значением '1' крайние точки, до которых есть только один путь:")
    k1 = 0
    for i in range(a - 2, -1, -1):
        grid[i][k1] = 1
        k1 += 1
    for j in range(b):
        grid[a-1][j] = 1
    showGrid(grid)

    print('Заполняем остальные точки как сумму левой и нижней точки:')
    k2 = 1
    for i in range(a - 2, -1, -1):
        for j in range(k2, b):
            grid[i][j] = grid[i][j - 1] + grid[i + 1][j]
        k2 += 1
    showGrid(grid)

    print(f'Количество путей: {grid[0][b - 1]}', end="\n\n")

# pathsCounter_1(15, 14)
pathsCounter_2(2, 2)
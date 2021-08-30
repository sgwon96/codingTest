def solution(m, n, puddles):
    grid = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    grid[m][n - 1] = 1

    for x in range(m - 1, -1, -1):
        for y in range(n - 1, -1, -1):
            if [x + 1, y + 1] not in puddles:
                grid[x][y] = grid[x + 1][y] + grid[x][y + 1]

    return grid[0][0] % 1000000007
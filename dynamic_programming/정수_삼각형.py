def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            max_path = 0
            if j > 0:
                max_path = max(max_path, triangle[i - 1][j - 1])
            if j != len(triangle[i]) - 1:
                max_path = max(max_path, triangle[i - 1][j])
            triangle[i][j] = max_path + triangle[i][j]

    return max(triangle[-1])
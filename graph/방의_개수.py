from collections import defaultdict


def move(arrow, x, y):
    direction = {0: (0, 1), 1: (1, 1), 2: (1, 0), 3: (1, -1), 4: (0, -1), 5: (-1, -1),
                 6: (-1, 0), 7: (-1, 1)}

    return x + direction[arrow][0], y + direction[arrow][1]


def solution(arrows):
    x, y = 0, 0
    path = defaultdict(set)
    path[(x, y)] = set()
    answer = 0
    for arrow in arrows:
        for _ in range(2):
            nx, ny = move(arrow, x, y)
            if (nx, ny) in path and (x, y) not in path[(nx, ny)]:
                answer += 1

            path[(nx, ny)].add((x, y))
            path[(x, y)].add((nx, ny))
            x, y = nx, ny
    return answer
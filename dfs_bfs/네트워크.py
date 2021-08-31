from collections import defaultdict


def solution(n, computers):
    connections = defaultdict(set)

    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                connections[i].add(j)

    visited = set()
    count = 0
    for i in range(n):
        if i not in visited:
            new_network = dfs(connections, i)
            visited = visited.union(new_network)
            count += 1

    return count


def dfs(network, start):
    visited = set()
    stack = list(network[start])

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(list(network[node]))

    return visited
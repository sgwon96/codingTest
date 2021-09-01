from collections import defaultdict, deque


def solution(n, edge):
    graph = defaultdict(set)

    for a, b in edge:
        graph[a].add(b)
        graph[b].add(a)

    queue = deque([[1, 0]])
    visited = dict()
    visited[1] = 0

    while queue:
        node, distance = queue.popleft()
        for connected_node in graph[node]:
            if connected_node not in visited:
                queue.append([connected_node, distance + 1])
                visited[connected_node] = distance + 1

    count = 0
    for num in visited:
        if visited[num] == distance:
            count += 1

    return count
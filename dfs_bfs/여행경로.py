from collections import defaultdict


def solution(tickets):
    graph = defaultdict(lambda: list())

    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])

    for city in graph:
        graph[city].sort(reverse=True)

    path = []
    stack = ["ICN"]

    while stack:
        city = stack[-1]
        if graph[city]:
            stack.append(graph[city].pop())
        else:
            path.append(stack.pop())

    path.reverse()
    return path
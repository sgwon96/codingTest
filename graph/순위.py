from collections import defaultdict


def solution(n, results):
    winner_table = lambda: [set(), set()]
    winner_graph = defaultdict(winner_table)

    for a, b in results:
        winner_graph[a][1].add(b)
        winner_graph[b][0].add(a)

    for i in range(1, n + 1):
        for player in winner_graph[i][0]:  # i > player
            winner_graph[player][1].update(winner_graph[i][1])
        for player in winner_graph[i][1]:
            winner_graph[player][0].update(winner_graph[i][0])

    answer = 0
    for player in winner_graph:
        if len(winner_graph[player][0]) + len(winner_graph[player][1]) == n - 1:
            answer += 1

    return answer
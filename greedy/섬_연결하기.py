def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    roads = set((costs[0][0], costs[0][1]))
    answer = costs[0][2]

    while n != len(roads):
        for i, (start, end, cost) in enumerate(costs[1:]):
            a = start in roads
            b = end in roads

            if (a and not b) or (not a and b):
                answer += cost
                roads.add(start)
                roads.add(end)
                break

    return answer
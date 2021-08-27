def solution(prices):
    n = len(prices)
    answer = [0 for i in range(len(prices))]

    for i in range(n):
        for j in range(i + 1, n):
            if prices[i] > prices[j]:
                answer[i] = j - i
                break
        if answer[i] == 0:
            answer[i] = n - 1 - i

    return answer
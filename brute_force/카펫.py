def solution(brown, yellow):
    answer = []
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            w = yellow / i
            h = i
            if (w + 2) * (h + 2) - yellow == brown:
                answer = [w + 2, h + 2]
                break

    return answer
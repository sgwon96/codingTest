def solution(n, times):
    start = 1
    end = n * times[0]

    while start < end:
        middle = (start + end) // 2
        examined = 0
        for time in times:
            examined += middle // time

        if examined >= n:
            end = middle
        else:
            start = middle + 1
    return start
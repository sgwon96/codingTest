def solution(distance, rocks, n):
    rocks = [0] + rocks + [distance]
    rocks.sort()
    spaces = [rocks[i + 1] - rocks[i] for i in range(len(rocks) - 1)]

    start = 1
    end = distance

    while start <= end:
        mid = (start + end) // 2
        count = 0
        space = 0
        for s in spaces:
            space += s
            if space < mid:
                count += 1
            else:
                space = 0

        if count > n:
            end = mid - 1
        else:
            start = mid + 1

    return start - 1
def solution(numbers, target):
    possible_sums = [-numbers[0], numbers[0]]

    for num in numbers[1:]:
        sums = []
        for s in possible_sums:
            sums.append(s + num)
            sums.append(s - num)
        possible_sums = sums

    answer = 0
    for s in possible_sums:
        if s == target:
            answer += 1

    return answer
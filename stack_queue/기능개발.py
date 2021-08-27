import math
from collections import deque


def solution(progresses, speeds):
    answer = []
    days_left = []
    deployed = 0

    for i, p in enumerate(progresses):
        day = (100 - p) / speeds[i]
        day = math.ceil(day)
        days_left.append(day)

    count = 0
    deploy_date = days_left[0]
    days_left = deque(days_left)

    while days_left:
        date = days_left.popleft()
        if date <= deploy_date:
            count += 1
        else:
            answer.append(count)
            deploy_date = date
            count = 1
    answer.append(count)

    return answer
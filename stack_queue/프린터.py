from collections import deque


def solution(priorities, location):
    for i in range(len(priorities)):
        priorities[i] = (priorities[i], i)

    priorities = deque(priorities)

    order = 0
    while len(priorities) > 0:
        highest = max(priorities, key=lambda x: x[0])[0]
        priority, i = priorities.popleft()

        if priority == highest:
            order += 1
            if i == location:
                break
        else:
            priorities.append((priority, i))

    return order
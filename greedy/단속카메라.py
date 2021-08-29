from copy import copy


def solution(routes):
    road = []

    for i, (begin, end) in enumerate(routes):
        road.append((begin, 'b', i))
        road.append((end, 'e', i))

    road.sort(key=lambda x: (x[0], x[1]))

    answer = 0
    watching = set()
    cars_in_vision = set()
    for x, x_type, car in road:
        if x_type == 'b':
            cars_in_vision.add(car)
        elif car not in watching:
            answer += 1
            watching = watching.union(cars_in_vision)
            cars_in_vision = set()

    return answer
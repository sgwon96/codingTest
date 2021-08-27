from collections import deque


def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    trucks_on_bridge = deque([])

    total_weight = 0
    total_time = 0
    while truck_weights or trucks_on_bridge:

        total_time += 1
        for i in range(len(trucks_on_bridge)):
            trucks_on_bridge[i][1] += 1

        if trucks_on_bridge and trucks_on_bridge[0][1] >= bridge_length:
            truck_weight, time = trucks_on_bridge.popleft()
            total_weight -= truck_weight

        if truck_weights and truck_weights[0] + total_weight <= weight:
            truck_weight = truck_weights.popleft()
            total_weight += truck_weight
            trucks_on_bridge.append([truck_weight, 0])

    return total_time
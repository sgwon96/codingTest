def solution(bridge_length, weight, truck_weights):
    t = 1
    bridge = [0 for i in range(bridge_length)]
    bridge[-1] = truck_weights.pop(0)
    total_weights = bridge[-1]
    
    while total_weights > 0:
        t += 1
        total_weights -= bridge[0]
        bridge = bridge[1:]
        bridge.append(0)
        
        if len(truck_weights) > 0 and total_weights + truck_weights[0] <= weight:
            bridge[-1] = truck_weights.pop(0)
            total_weights += bridge[-1]

    return t
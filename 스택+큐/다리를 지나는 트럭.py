def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0 for i in range(bridge_length)]
    
    while len(truck_weights) > 0:
        answer += 1
        bridge.pop(0)
        
        if sum(bridge) + truck_weights[0] > weight:
            bridge.append(0)
            
        else:
            bridge.append(truck_weights[0])
            truck_weights.pop(0)
            
    answer += bridge_length
    
    return answer

def solution(n, lost, reserve):
    clothes = {i : 1 for i in range(1, n+1)}
    
    for i in lost:
        clothes[i] -= 1
        
    for i in reserve:
        clothes[i] += 1

    participant = 0
    for i in clothes:
        if clothes[i] >= 1:
            participant += 1
            continue
        
        # lost
        if i != 1 and clothes[i-1] == 2: #borrow
            clothes[i-1] -= 1
            clothes[i] += 1
            participant += 1
        
        elif i != n and clothes[i+1] == 2: #borrow
            clothes[i+1] -= 1
            clothes[i] += 1
            participant += 1
    
    return participant
def solution(name):
    name = list(name)
    completed = ["A" for i in range(len(name))]
    
    answer = 0
    cursor = 0
    while True:
        answer += upDown(name[cursor])
        completed[cursor] = name[cursor]
        
        moveTo = leftRight(name, completed, cursor)
        # print("leftRight", moveTo)
        answer += abs(moveTo)
        
        if moveTo == 0:
            break
            
        cursor = (cursor + len(name) + moveTo) % len(name)
        
    return answer

def upDown(c):
    greedy = min(ord(c) - ord("A"), ord("Z") + 1 - ord(c))
    # print("upDown", greedy)
    return greedy

def leftRight(name, completed, baseIdx):
    if len(name) == 1:
        return 0
    
    left, right = 1, 1
    
    # left
    i = baseIdx - 1
    while True:
        i = (i + len(name)) % len(name)
        
        if i == baseIdx or name[i] != completed[i]: # fullturn or find one to move
            break
            
        i -= 1
        left += 1
    
    # right
    i = baseIdx + 1
    while True:
        i = i % len(name)
        
        if i == baseIdx or name[i] != completed[i]:
            break
        
        i += 1
        right += 1
    
    if left == len(name) and right == len(name): # nothing to change
        return 0
    
    if left < right:
        return - left
    else:
        return right
        
    
print(solution("JEROEN"))
def solution(priorities, location):
    printed = 0
    
    while len(priorities) > 0:
        print(location, priorities)
        if len(priorities) == 1:
            return printed + 1
        
        if priorities[0] >= max(priorities[1:]): # print
            printed += 1
            
            if location == 0:
                return printed
            
            location -= 1
            priorities.pop(0)
            
        else: # move
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
            
            priorities.append(priorities.pop(0))
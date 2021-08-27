import math

def solution(progresses, speeds):
    answer = []
    left = []
    done = 0
    for i in range(len(progresses)):
        left.append(math.ceil((100 - progresses[i]) / speeds[i]))
        
    day = left[0]
    for i in range(len(left)):
        if left[i] <= day:
            done += 1
        else:
            day = left[i]
            answer.append(done)
            done = 1
            
    answer.append(done)
    
    return answer

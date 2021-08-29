def solution(name):
    answer, i = 0, 0
    upDown = []
    for n in name:
        upDown.append(min(ord(n)-ord('A'), ord('Z')-ord(n)+1))
    
    while True:
        answer += upDown[i]
        upDown[i] = 0
        if sum(upDown) == 0:
            break
        
        left, right = 1, 1
        while upDown[i-left] == 0:
            left += 1
        while upDown[i+right] == 0:
            right += 1
        
        if left < right:
            i -= left
            answer += left
        else:
            i += right
            answer += right
            
    return answer

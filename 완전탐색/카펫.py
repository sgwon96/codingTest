def solution(brown, yellow):
    answer = []
    for width in range(1, int(brown/2)):
        height = int(brown/2) - width + 2
        if width < height:
            continue
            
        yWidth = width - 2
        yHeight = height - 2
        
        if yWidth * yHeight == yellow:
            answer.append(width)
            answer.append(height)
            break
            
    return answer

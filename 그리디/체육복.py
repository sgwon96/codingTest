def solution(n, lost, reserve):
    answer = 0
    # 여벌을 가져왔지만 도난당함
    reserveLost = [x for x in reserve if x not in lost]
    # 순수히 도난 당해서 체육복이 없는 사람
    realLost = [x for x in lost if x not in reserve]
    
    for spare in reserveLost:
        # 바로 앞번호나 뒷번호에게만 빌려줄 수 있음
        if spare-1 in realLost:
            realLost.remove(spare-1)
        elif spare+1 in realLost:
            realLost.remove(spare+1)
    answer = n - len(realLost)
    
    return answer

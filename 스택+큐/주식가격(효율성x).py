def solution(prices):
    answer = []
    before = 0
    flag = True
    while len(prices) > 1:
        flag = True
        time = 0
        before = prices.pop(0)
        for p in prices:
            time += 1
            if before > p:
                answer.append(time)
                flag = False
                break
        if flag:
            answer.append(time)
            
    answer.append(0)
            
    return answer

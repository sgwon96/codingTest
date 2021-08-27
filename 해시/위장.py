def solution(clothes):
    answer = 1
    wear = {}
    for c in clothes:
        # 옷 종류 당 몇개 있는지 저장
        wear[c[1]] = wear.get(c[1],0) + 1
    for w in wear:
        # 안 입을 경우 +1 해서 경우의 수 계산
        answer *= wear[w] + 1

    # 아무것도 안 입을 경우 제외    
    answer -= 1
            
    return answer

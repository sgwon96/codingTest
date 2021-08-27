def solution(participant, completion):
    answer = ''
    runner = {} # 선수들 상태 저장할 dictionary
    for p in participant:
        # 참여했으면 +1
        runner[p] = runner.get(p,0) + 1 # (동명이인 방지) 선수들 상태 + 1
    for c in completion:
        # 완주했으면 -1
        runner[c] -= 1
    for r in runner:
        print(runner[r])
        # 완주하지 못했을 경우 answer
        if runner[r] != 0:
            answer += r
            
    return answer

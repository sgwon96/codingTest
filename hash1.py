def solution(participant, completion):
    comp_map = {}
    for c in completion:
        if c in comp_map:
            comp_map[c] += 1
        else:
            comp_map[c] = 1

    answer = ''
    for p in participant:
        if p not in comp_map or comp_map[p] == 0:
            answer = p
            break
        else:
            comp_map[p] -= 1
    
    return answer
def solution(priorities, location):
    answer = 0
    index = []
    highest = priorities[0]
    while(len(priorities) > 0):
        if priorities[0] < max(priorities):
            priorities.append(priorities.pop(0))
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
        else:
            priorities.pop(0)
            answer += 1
            if location == 0:
                return answer
            location -= 1

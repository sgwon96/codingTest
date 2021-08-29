def solution(answers):
    answer = []
    ansA = [1, 2, 3, 4, 5]
    ansB = [2, 1, 2, 3, 2, 4, 2, 5]
    ansC = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    A, B, C = 0, 0, 0
    
    for i in range(len(answers)):
        if ansA[i%5] == answers[i]:
            A += 1
        if ansB[i%8] == answers[i]:
            B += 1
        if ansC[i%10] == answers[i]:
            C += 1
    
    winner = max(A, B, C)
    
    if winner == A:
        answer.append(1)
    if winner == B:
        answer.append(2)
    if winner == C:
        answer.append(3)
    
    return answer

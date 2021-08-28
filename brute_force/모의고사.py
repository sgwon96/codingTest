def solution(answers):
    a_answers = [1, 2, 3, 4, 5]
    b_answers = [2, 1, 2, 3, 2, 4, 2, 5]
    c_answers = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    scores = [0, 0, 0]

    for i in range(len(answers)):
        if a_answers[i % 5] == answers[i]:
            scores[0] += 1
        if b_answers[i % 8] == answers[i]:
            scores[1] += 1
        if c_answers[i % 10] == answers[i]:
            scores[2] += 1

    answer = []
    max_score = max(scores)
    for i in range(3):
        if scores[i] == max_score:
            answer.append(i + 1)

    return answer
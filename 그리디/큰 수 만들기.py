def solution(number, k):
    # stack 이용
    answer = []
    answer.append(number[0])
    
    for num in number[1:]:
        while k > 0 and answer[-1] < num:
            answer.pop()
            k -= 1
            if not answer or k <= 0:
                break
        answer.append(num)
    
    if k != 0:
        answer = answer[:-k]
    
    return ''.join(answer)

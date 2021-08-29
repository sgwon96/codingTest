def solution(numbers):
    answer = ''
    
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x : x*3, reverse = True)
    answer = str(int(''.join(numbers))) # 000 처리
    
    return answer

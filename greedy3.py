def solution(number, k):
    nums = list(map(int, number))
    
    answer = ''
    maxIdx = 0
    for i in range(len(number) - k):
        print(i, nums[maxIdx + 1:k + i + 1])
        for j in range(maxIdx + 1, k + i + 1):
            if nums[j] > nums[maxIdx]:
                maxIdx = j
        
        answer += str(nums[maxIdx])
        maxIdx += 1
        
    return answer

print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))

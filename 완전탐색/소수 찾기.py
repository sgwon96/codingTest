from itertools import permutations

def solution(numbers):
    answer = 0
    nums = []

    for i in range(1, len(numbers)+1):
        perm = list(permutations(numbers, i))
        for j in perm:
            nums.append(int(''.join(j)))
    
    nums = list(set(nums))
    
    for n in nums:
        if n==0 or n==1:
            continue
        if n==2:
            answer += 1
        for i in range(2, n):
            if n%i == 0:
                break
            elif i == n-1:
                answer += 1
                
    return answer

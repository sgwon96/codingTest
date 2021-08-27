import heapq

def solution(jobs):
    jobNum = len(jobs)
    answer, now = 0, 0
    before = -1
    works = []
                
    while len(jobs) > 0:
        for j in jobs:
            if before < j[0] <= now:
                heapq.heappush(works, [j[1], j[0]])
        if len(works) > 0:
            cur_work = heapq.heappop(works)
            before = now
            now += cur_work[0]
            answer += now - cur_work[1]
            jobs.remove([cur_work[1], cur_work[0]])
        else:
            now += 1
    
#     for j in jobs:
#         heapq.heappush(works, [j[1], j[0]])
    
#     while len(works) > 0:
#         w = works[0]
#         if w[1] <= now:
#             heapq.heappop(works)
#             now += w[0]
#             answer += now - w[1]
#         else:
#             now += 1
    
    answer = int(answer/jobNum)
    
    return answer

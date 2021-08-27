import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while(scoville[0] < K):
        if len(scoville) == 1:
            return -1
        
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        newFood = first + (second*2)
        heapq.heappush(scoville, newFood)

        answer += 1
        
    return answer

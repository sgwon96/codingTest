import heapq

def solution(scoville, K):
    heapq.heapify(scoville)

    i = 0
    while scoville[0] < K:
        if len(scoville) < 2:
            i = -1
            break

        new_food = heapq.heappop(scoville) + 2 * heapq.heappop(scoville)
        heapq.heappush(scoville, new_food)
        i+=1

    return i
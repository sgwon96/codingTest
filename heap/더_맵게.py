import heapq


def solution(scoville, k):
    heapq.heapify(scoville)
    heap = scoville
    mix_count = 0
    while heap[0] < k:
        if len(heap) < 2:
            return -1
        heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
        mix_count += 1
    return mix_count
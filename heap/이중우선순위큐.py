import heapq


def solution(operations):
    heap = []
    for o in operations:
        o_type, num = o.split(' ')
        if o_type == 'I':
            heapq.heappush(heap, int(num))
        elif heap:
            if num == "1":
                heap.remove(max(heap))
            else:
                heapq.heappop(heap)

    if heap:
        answer = [max(heap), heap[0]]
    else:
        answer = [0, 0]

    return answer
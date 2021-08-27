import heapq

def solution(operations):
    answer = []
    minHeap = []
    maxHeap = []
    
    for o in operations:
        command = o.split()
        if command[0] == 'I':
            num = int(command[1])
            heapq.heappush(minHeap, num)
            heapq.heappush(maxHeap, (-num, num))
        elif command[0] == 'D':
            if len(minHeap) == 0:
                pass
            elif command[1] == '1':
                value = heapq.heappop(maxHeap)[1]
                minHeap.remove(value)
            elif command[1] == '-1':
                value = heapq.heappop(minHeap)
                maxHeap.remove((-value, value))
                
    if len(minHeap) == 0:
        return [0, 0]
    else:
        return [heapq.heappop(maxHeap)[1], heapq.heappop(minHeap)]

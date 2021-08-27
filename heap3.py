import heapq

def solution(operations):
    minHeap = []
    maxHeap = []
    
    for op in operations:
        cmd, num = op.split()
        num = int(num)
        
        if cmd == "I":
            heapq.heappush(minHeap, num)
            heapq.heappush(maxHeap, (-num, num))
            
        elif num == 1:
            heapq.heappop(maxHeap)
        
        else:
            heapq.heappop(minHeap)
    
    common = []
    for min_element in minHeap:
        for i in range(len(maxHeap)):
            if min_element == maxHeap[i]:
                common.append(maxHeap.pop(i))
                break
            
    if len(common)  == 0:
        return [0,0]
    else:
        return [max(common), min(common)]

def solution(jobs):
    num = len(jobs)

    for job in jobs:
        job.append(job[1] - job[0])
        
    answer = 0
    t = 0
    heap = [[]]
    
    while len(jobs) > 0 or len(heap) > 1:
        for i in range(len(jobs)-1, -1, -1):
            if jobs[i][0] <= t:
                heapPush(heap, jobs.pop(i))
        
        program = heapPop(heap)
        answer += t + program[1] - program[0]
        t += program[1]
        
    
    return int(answer / num)

def heapPop(heap):
    popped = heap[1]
    largest = heap.pop(-1)
    
    i = 1
    while i < len(heap):
        if i*2 + 1 < len(heap) and heap[i*2][2] < heap[i*2 + 1][2] and heap[i*2][2] < largest[2]:
            heap[i] = heap[i*2]
            i = i*2
        elif i*2 + 1 < len(heap) and heap[i*2][2] > heap[i*2 + 1][2] and heap[i*2+1][2] < largest[2]:
            heap[i] = heap[i*2 + 1]
            i = i*2 + 1
        elif i*2 < len(heap) and heap[i*2][2] < largest[2]:
            heap[i] = heap[i*2]
            heap[i*2] = largest
            break
        else:
            heap[i] = largest
            break
            
    return popped

def heapPush(heap, job):
    i = len(heap)
    heap.append([])
    
    while int(i / 2) > 0:
        parentIdx = int(i/2)
        
        if heap[parentIdx][2] > job[2]:
            heap[i] = heap[parentIdx]
            i = parentIdx
        else:
            break
            
    heap[i] = job
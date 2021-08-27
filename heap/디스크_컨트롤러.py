import heapq


def solution(jobs):
    len_jobs = len(jobs)
    jobs.sort(key=lambda x: x[0])
    answer = []
    time = jobs[0][0]
    queue = []

    while len(answer) < len_jobs:
        while jobs and time >= jobs[0][0]:
            queue.append(jobs.pop(0))

        if queue:
            queue.sort(key=lambda x: x[1])
            r_time, w_time = queue.pop(0)
            time += w_time
            answer.append(time - r_time)
        else:
            time += 1

    return sum(answer) // len(answer)
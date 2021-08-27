import math

def solution(progresses, speeds):
    releases = []
    dates = [getDate(progresses[i], speeds[i]) for i in range(len(progresses))]
    
    maxDate = dates[0]
    count = 1
    
    for i in range(1, len(dates)):
        if dates[i] > maxDate:
            releases.append(count)
            maxDate = dates[i]
            count = 0
            
        count += 1
    
    if len(dates) > len(releases):
        releases.append(count)

    return releases

def getDate(progress, speed):
    result = math.ceil((100 - progress) / speed)
    return result
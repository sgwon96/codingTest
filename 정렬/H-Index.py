def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    paperNum = len(citations)
    for i in range(paperNum):
        count = 0
        for c in citations:
            if c >= paperNum-i:
                count += 1
            if count >= paperNum-i:
                return paperNum-i
    return 0
